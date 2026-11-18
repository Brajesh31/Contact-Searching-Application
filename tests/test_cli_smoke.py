#!/usr/bin/env python3
"""Exercise the real CLI using disposable synthetic contact data."""
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile


INITIAL_CONTACT = "Alex Example,5550101234,alex@example.invalid"
ADDED_CONTACT = "Taylor Sample,5550109876,taylor@example.invalid"
MENU_INPUT = (
    "1\n"
    "Taylor Sample\n"
    "5550109876\n"
    "taylor@example.invalid\n"
    "5\n"
    "Taylor Sample\n"
    "6\n"
    "alex\n"
    "3\n"
    "Taylor Sample\n"
    "8\n"
)


def fail(message: str, stdout: str = "", stderr: str = "") -> int:
    print(f"FAIL: {message}", file=sys.stderr)
    if stdout:
        print("--- stdout ---", file=sys.stderr)
        print(stdout, file=sys.stderr)
    if stderr:
        print("--- stderr ---", file=sys.stderr)
        print(stderr, file=sys.stderr)
    return 1


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python3 tests/test_cli_smoke.py <compiled-executable>", file=sys.stderr)
        return 2

    executable = Path(sys.argv[1]).expanduser()
    if not executable.is_absolute():
        executable = (Path.cwd() / executable).resolve()
    if not executable.is_file():
        return fail(f"compiled executable not found: {executable}")

    with tempfile.TemporaryDirectory(prefix="contact-cli-smoke-") as temp:
        workdir = Path(temp)
        test_executable = workdir / "contact-search"
        shutil.copy2(executable, test_executable)
        data_file = workdir / "contacts.txt"
        data_file.write_text(INITIAL_CONTACT + "\n", encoding="utf-8")

        try:
            result = subprocess.run(
                [str(test_executable)],
                input=MENU_INPUT,
                text=True,
                capture_output=True,
                cwd=workdir,
                timeout=15,
                check=False,
            )
        except subprocess.TimeoutExpired:
            return fail("application did not finish within 15 seconds")

        if result.returncode != 0:
            return fail(
                f"application exited with status {result.returncode}",
                result.stdout,
                result.stderr,
            )

        expected_output = (
            "Name: Taylor Sample, Phone Number: 5550109876, "
            "Email: taylor@example.invalid"
        )
        if expected_output not in result.stdout:
            return fail("exact name search did not print the added contact", result.stdout, result.stderr)
        if "Found contacts:" not in result.stdout or "Alex Example" not in result.stdout:
            return fail("case-insensitive partial-name search did not find the initial contact", result.stdout, result.stderr)
        if "Contact exported as Taylor Sample.vcf successfully." not in result.stdout:
            return fail("export success message was not printed", result.stdout, result.stderr)

        rows = set(data_file.read_text(encoding="utf-8").splitlines())
        if INITIAL_CONTACT not in rows or ADDED_CONTACT not in rows:
            return fail("the temporary contacts.txt did not retain both records", result.stdout, result.stderr)

        vcard_path = workdir / "Taylor Sample.vcf"
        if not vcard_path.is_file():
            return fail("expected vCard export file was not created", result.stdout, result.stderr)
        vcard = vcard_path.read_text(encoding="utf-8")
        for marker in (
            "BEGIN:VCARD",
            "VERSION:3.0",
            "FN:Taylor Sample",
            "TEL;TYPE=CELL:5550109876",
            "EMAIL;TYPE=INTERNET:taylor@example.invalid",
            "END:VCARD",
        ):
            if marker not in vcard:
                return fail(f"vCard export is missing expected field: {marker}", result.stdout, result.stderr)

        print("--- Captured CLI session using synthetic data ---")
        print(result.stdout.rstrip())

    print("PASS: startup contact loading and add operation.")
    print("PASS: exact name search and case-insensitive partial-name search.")
    print("PASS: updated records persisted in the temporary contact file.")
    print("PASS: vCard 3.0 export contains the expected contact fields.")
    print("PASS: tracked repository data was not used or modified.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

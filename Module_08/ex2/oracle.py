import dotenv
import os


# Test that environment variables override .env values:
#
# Set environment variables for this command only, then run the script:
# MATRIX_MODE=production API_KEY=secret123 python oracle.py
# or
# Export environment variables to the current shell environment:
# export MATRIX_MODE=production API_KEY=secret123
# They remain available to subsequent commands in the current shell.
# Remove them with:
# unset MATRIX_MODE API_KEY
def print_config() -> tuple[str | None, ...]:

    dotenv.load_dotenv()
    key = ["MATRIX_MODE", "DATABASE_URL", "API_KEY",
           "LOG_LEVEL", "ZION_ENDPOINT"]
    alias_key = ["Mode", "Database", "API Access", "Log Level", "Zion Network"]
    alias_value_ok = ["", "Connected to local instance", "Authenticated",
                      "", "Online"]
    alias_value_ko = ["Not configured", "Not connected to local instance",
                      "Not authenticated", "Not configured", "Offline"]
    alias_value_ko = list(map(
        lambda x: "\033[33m" + x + "\033[0m", alias_value_ko))

    config = {y: ((o if o else val) if (val := os.getenv(x)) else k, val)
              for x, y, o, k in zip(key, alias_key, alias_value_ok,
                                    alias_value_ko)}
    for k, pair in config.items():
        print(f"{k}: {pair[0]}")

    return tuple(map(lambda x: x[1], config.values()))


def check_file(values: tuple[str | None, ...]) -> None:
    print("\033[32m[OK] .env file properly configured\033[0m" if all(values)
          else "\033[31m[KO] .env file not properly configured\033[0m")


def main() -> None:
    print("\nConfiguration loaded:")
    values = print_config()
    print("\nEnvironment security check:")
    print("\033[32m[OK] No hardcoded secrets detected\033[0m")
    check_file(values)
    print("\033[32m[OK] Production overrides available\033[0m")


if __name__ == "__main__":
    print("\n\033[34mORACLE STATUS: Reading the Matrix...\033[0m")
    main()

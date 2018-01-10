#!/usr/bin/env python
import time
import subprocess
import pathlib
import hashlib

here = pathlib.Path('.')


def path_identity(path):
    content_hash = hashlib.md5(path.read_bytes()).hexdigest()

    return (path, content_hash)


def get_identities(start_path, pattern):
    return set(
        path_identity(path)
        for path in start_path.glob(pattern)
        if path.exists()
    )


def main():
    known_identities = get_identities(here, '*.py')
    subprocess.call(['python', '-m', 'unittest'])

    try:
        while True:
            new_identities = get_identities(here, '*.py')
            diff = known_identities.symmetric_difference(new_identities)

            if diff:
                subprocess.call(['python', '-m', 'unittest'])

            known_identities = new_identities
            time.sleep(.25)
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()

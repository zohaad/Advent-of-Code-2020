from pathlib import Path
from functools import reduce
import re

passports = Path("inputs/4.txt").read_text().split("\n\n")


def destruct(passport):
    passport = passport.replace("\n", " ").split(" ")
    return {k: v for k, v in (kv.split(":") for kv in passport)}


def valid(passport):
    fields = [
        "byr",
        "iyr",
        "eyr",
        "hgt",
        "hcl",
        "ecl",
        "pid",
        # optional field: 'cid',
    ]

    return all(k in passport for k in fields)


print("part 1:", sum(map(valid, (destruct(passport) for passport in passports))))

# part 2


def valid2(passport):
    if not valid(passport):
        return False

    # birth year
    if not 1920 <= int(passport["byr"]) <= 2002:
        return False

    # issue year
    if not 2010 <= int(passport["iyr"]) <= 2020:
        return False

    # expiration year
    if not 2020 <= int(passport["eyr"]) <= 2030:
        return False

    # height must be 150-193cm or 59-76in
    if (
        re.match(r"^(1[5-8][0-9]|19[0-3])cm|(59|6[0-9]|7[0-6])in$", passport["hgt"])
        is None
    ):
        return False

    # hair color must be a hex color code
    if re.match(r"^#[0-9a-f]{6}$", passport["hcl"]) is None:
        return False

    # eye color
    if passport["ecl"] not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
        return False

    # passport id must be a 9-digit number, can have leading 0's
    if re.match(r"^[0-9]{9}$", passport["pid"]) is None:
        return False

    return True


print("part 2:", sum(map(valid2, (destruct(passport) for passport in passports))))

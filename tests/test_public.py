"""PUBLIC sample tests for COMP1205 Assignment #2.

These tests are copied from the sample runs in the handout. Passing them shows
your program matches the samples; it does NOT guarantee full marks - the
hidden tests check many more cases (see "Edge cases tested" for each part).

DO NOT EDIT OR DELETE THIS FILE. Changes are detected and penalised.

Run:  python -m pytest tests/test_public.py -v
"""
import subprocess
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
TIMEOUT = 2


def run_program(part, stdin_lines):
    """Run partname.py with the given input lines and return its stdout."""
    path = REPO / f"{part}.py"
    result = subprocess.run([sys.executable, str(path)], input="\n".join(stdin_lines) + "\n",
                            capture_output=True, text=True, timeout=TIMEOUT, cwd=str(REPO))
    assert result.returncode == 0, "Your program crashed:\n" + result.stderr[-1500:]
    return result.stdout


def tidy(text):
    """Remove trailing spaces from every line and trailing blank lines."""
    return "\n".join(line.rstrip() for line in text.rstrip().splitlines())


# (part, sample number, input lines, exact expected stdout - prompts included,
#  because your typed input is NOT echoed when input comes from a test)
SAMPLES = [
    ('q1_part1', 1,
     ['p 1234'],
     (
      'Enter plate: Normalised plate: P1234\n'
      'Status: VALID\n')),
    ('q1_part1', 2,
     ['AB0123'],
     (
      'Enter plate: Normalised plate: AB0123\n'
      'Status: INVALID\n')),
    ('q1_part2', 1,
     ['r-2026'],
     (
      'Enter plate: Normalised plate: R2026\n'
      'Status: VALID\n'
      'Category: Rental\n'
      'Island: Antigua\n')),
    ('q1_part2', 2,
     ['kx 12'],
     (
      'Enter plate: Normalised plate: KX12\n'
      'Status: INVALID\n')),
    ('q1_part3', 1,
     [' t-482 ', 't4##'],
     (
      'Enter plate: Normalised plate: T482\n'
      'Status: VALID\n'
      'Category: Taxi\n'
      'Island: Antigua\n'
      'Enter watch-list pattern: Watch-list: FLAGGED\n')),
    ('q1_part3', 2,
     ['gx 1205', 'G?12#'],
     (
      'Enter plate: Normalised plate: GX1205\n'
      'Status: VALID\n'
      'Category: Government\n'
      'Island: Barbuda\n'
      'Enter watch-list pattern: Watch-list: CLEAR\n')),
    ('q2_part1', 1,
     ['120', '12.5', '14.50'],
     (
      'Trip distance (km): Fuel efficiency (km per litre): Price per gallon (EC$): Fuel used: 9.60 litres\n'
      'Fuel cost: EC$36.78\n')),
    ('q2_part1', 2,
     ['35', '9', '15.25'],
     (
      'Trip distance (km): Fuel efficiency (km per litre): Price per gallon (EC$): Fuel used: 3.89 litres\n'
      'Fuel cost: EC$15.67\n')),
    ('q2_part2', 1,
     ['abc', '120', '-5', '0', '12.5', '14.50'],
     (
      'Trip distance (km): Invalid: enter a number greater than 0.\n'
      'Trip distance (km): Fuel efficiency (km per litre): Invalid: enter a number greater than 0.\n'
      'Fuel efficiency (km per litre): Invalid: enter a number greater than 0.\n'
      'Fuel efficiency (km per litre): Price per gallon (EC$): Fuel used: 9.60 litres\n'
      'Fuel cost: EC$36.78\n')),
    ('q2_part2', 2,
     ['35', '9', '1.2.3', '15.25'],
     (
      'Trip distance (km): Fuel efficiency (km per litre): Price per gallon (EC$): Invalid: enter a number greater than 0.\n'
      'Price per gallon (EC$): Fuel used: 3.89 litres\n'
      'Fuel cost: EC$15.67\n')),
    ('q2_part3', 1,
     ['120', '12.5', '14.50', '40'],
     (
      'Trip distance (km): Fuel efficiency (km per litre): Price per gallon (EC$): Fare charged (EC$): Fuel used: 9.60 litres\n'
      'Fuel cost: EC$36.78\n'
      'Fare: EC$40.00\n'
      'Result: PROFIT of EC$3.22\n')),
    ('q2_part3', 2,
     ['35', '9', '15.25', '10.00'],
     (
      'Trip distance (km): Fuel efficiency (km per litre): Price per gallon (EC$): Fare charged (EC$): Fuel used: 3.89 litres\n'
      'Fuel cost: EC$15.67\n'
      'Fare: EC$10.00\n'
      'Result: LOSS of EC$5.67\n')),
    ('q3_part1', 1,
     ['SJ-THF-14', 'sg-bur-02', 'SJ-XYZ-10', 'BA-ASL-24', 'end'],
     (
      'Report (END to finish): Report (END to finish): Report (END to finish): Report (END to finish): Report (END to finish): Valid reports: 2\n'
      'Invalid reports: 2\n')),
    ('q3_part1', 2,
     [' sm-van-21 ', 'SM-VAN-21 x', 'END'],
     (
      'Report (END to finish): Report (END to finish): Report (END to finish): Valid reports: 1\n'
      'Invalid reports: 1\n')),
    ('q3_part2', 1,
     ['SJ', 'SJ-THF-14', 'SG-BUR-02', 'sj-asl-09', 'SJ-THF-23', 'SJ-BUR-30', 'END'],
     (
      'Parish code: Report (END to finish): Report (END to finish): Report (END to finish): Report (END to finish): Report (END to finish): Report (END to finish): Valid reports: 4\n'
      'Invalid reports: 1\n'
      'Parish SJ total: 3\n'
      'THF: 2\n'
      'BUR: 0\n'
      'ASL: 1\n'
      'TRF: 0\n'
      'VAN: 0\n'
      'Most common type: THF\n')),
    ('q3_part2', 2,
     ['bb', 'ba', 'SJ-TRF-10', 'END'],
     (
      'Parish code: Unknown parish code. Try again.\n'
      'Parish code: Report (END to finish): Report (END to finish): Valid reports: 1\n'
      'Invalid reports: 0\n'
      'Parish BA total: 0\n'
      'THF: 0\n'
      'BUR: 0\n'
      'ASL: 0\n'
      'TRF: 0\n'
      'VAN: 0\n'
      'Most common type: NONE\n')),
    ('q3_part3', 1,
     ['SJ', 'SJ-THF-14', 'SJ-ASL-03', 'SG-BUR-02', 'SJ-TRF-22', 'SJ-TRF-31', 'SJ-VAN-18', 'END'],
     (
      'Parish code: Report (END to finish): Report (END to finish): Report (END to finish): Report (END to finish): Report (END to finish): Report (END to finish): Report (END to finish): Valid reports: 5\n'
      'Invalid reports: 1\n'
      'Parish SJ total: 4\n'
      'THF: 1\n'
      'BUR: 0\n'
      'ASL: 1\n'
      'TRF: 1\n'
      'VAN: 1\n'
      'Most common type: THF\n'
      'Earliest hour: 03\n'
      'Latest hour: 22\n'
      'Longest streak: 2\n')),
    ('q3_part3', 2,
     ['SP', 'SJ-THF-14', 'END'],
     (
      'Parish code: Report (END to finish): Report (END to finish): Valid reports: 1\n'
      'Invalid reports: 0\n'
      'Parish SP total: 0\n'
      'THF: 0\n'
      'BUR: 0\n'
      'ASL: 0\n'
      'TRF: 0\n'
      'VAN: 0\n'
      'Most common type: NONE\n'
      'Earliest hour: N/A\n'
      'Latest hour: N/A\n'
      'Longest streak: 0\n')),
    ('q4_part1', 1,
     ['ke-20417-6'],
     (
      'Enter credential code: Credential: KE-20417-6\n'
      'Format: OK\n')),
    ('q4_part1', 2,
     ['KE 20417 6'],
     (
      'Enter credential code: Credential: KE 20417 6\n'
      'Format: BAD\n')),
    ('q4_part2', 1,
     ['KE-20417-6'],
     (
      'Enter credential code: Credential: KE-20417-6\n'
      'Format: OK\n'
      'Checksum: PASS\n')),
    ('q4_part2', 2,
     ['jm-41870-7'],
     (
      'Enter credential code: Credential: JM-41870-7\n'
      'Format: OK\n'
      'Checksum: FAIL (expected 1)\n')),
    ('q4_part3', 1,
     ['ag-21105-5', 'retreat'],
     (
      'Enter credential code: Credential: AG-21105-5\n'
      'Format: OK\n'
      'Checksum: PASS\n'
      'Role: Minister\n'
      'Zone requested: Access: GRANTED\n')),
    ('q4_part3', 2,
     ['UK-40404-7', ' Plenary '],
     (
      'Enter credential code: Credential: UK-40404-7\n'
      'Format: OK\n'
      'Checksum: PASS\n'
      'Role: Media\n'
      'Zone requested: Access: DENIED\n')),
    ('q5_part1', 1,
     ['3', '60 10', '30 25', '0 40'],
     (
      'Number of log entries: Entry 1 (speed minutes): Entry 2 (speed minutes): Entry 3 (speed minutes): Distance: 17.50 km\n')),
    ('q5_part1', 2,
     ['2', ' 45   20 ', '90 30'],
     (
      'Number of log entries: Entry 1 (speed minutes): Entry 2 (speed minutes): Distance: 30.00 km\n')),
    ('q5_part2', 1,
     ['3', '60 10', '95 20', '70 32'],
     (
      'Number of log entries: Entry 1 (speed minutes): Entry 2 (speed minutes): Entry 3 (speed minutes): Distance: 39.83 km\n'
      'Segments over 80 km/h: 1\n')),
    ('q5_part2', 2,
     ['3', '60 10', '50 8', '70 20'],
     (
      'Number of log entries: Entry 1 (speed minutes): Entry 2 (speed minutes): Invalid entry 2.\n')),
]


@pytest.mark.parametrize("sample", SAMPLES, ids=[f"{s[0]}_sample{s[1]}" for s in SAMPLES])
def test_sample_run(sample):
    part, _number, stdin_lines, expected = sample
    actual = run_program(part, stdin_lines)
    assert tidy(actual) == tidy(expected), (
        "Output differs from the handout sample run.\n--- expected ---\n" + tidy(expected)
        + "\n--- yours ---\n" + tidy(actual))

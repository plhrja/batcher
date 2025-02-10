import pytest
import json
from batcher import batcher

def test_batch_returns_empty_list_for_empty_input():
  assert batcher.batch([]) == []

def test_batch_should_raise_type_error_for_none_input():
  with pytest.raises(TypeError):
    batcher.batch(None)

@pytest.fixture(scope='module')
def long_range_input():
  return [str(k) for k in range(1024)]

def test_batch_should_batch_records_in_max_500_record_batches(long_range_input):
  batches = batcher.batch(long_range_input)
  assert len(batches) == 3
  assert len(batches[0]) == 500
  assert len(batches[1]) == 500
  assert len(batches[2]) == 24

def test_batch_should_maintain_order_of_records(long_range_input):
  batches = batcher.batch(long_range_input)
  assert batches[0] + batches[1] + batches[2] == long_range_input

@pytest.mark.parametrize("input_file", [
  "tests/testdata/should_filter_too_long_ascii_input.json",
  "tests/testdata/should_filter_too_long_special_characters_input.json",
  "tests/testdata/should_include_1mb_ascii_input.json",
  "tests/testdata/should_include_1mb_special_character_input.json",
  "tests/testdata/should_maintain_order_over_optimal_filling.json"
])
def test_batch_should_batch_according_to_testdata_configurationd(input_file: str):
  with open(input_file, encoding="utf-8") as file:
    data = json.load(file)
    batches = batcher.batch(data["input"])
    assert batches == data["expected"]
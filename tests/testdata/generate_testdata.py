import random
import string
import json

def generate_should_filter_too_long_ascii_input():
  data = "".join(random.choices(string.ascii_lowercase, k=int(1e6) + 1))
  write_to_file([data], [], "should_filter_too_long_ascii_input.json")

def generate_should_filter_too_long_special_characters_input():
  hiragana_range = [chr(k) for k in range(12353, 12438)]  # Hiraganas are represented with 3 bytes
  data = "".join(random.choices(hiragana_range, k=int(1e6 / 3) + 1))
  write_to_file([data], [], "should_filter_too_long_special_characters_input.json")

def generate_should_include_1mb_ascii_input():
  data = "".join(random.choices(string.ascii_lowercase, k=int(1e6)))
  write_to_file([data], [[data]], "should_include_1mb_ascii_input.json")

def generate_should_include_1mb_special_character_input():
  hiragana_range = [chr(k) for k in range(12353, 12438)]
  data = "".join(random.choices(hiragana_range, k=int(1e6 / 3)))
  write_to_file([data], [[data]], "should_include_1mb_special_character_input.json")

def generate_should_maintain_order_over_optimal_filling():
  head = ["a", "b", "c", "d"]
  mid = [
    "".join(random.choices(string.ascii_lowercase, k=int(1e6))) 
      for _ in range(9)
  ]
  tail = ["1", "2", "3", "4"]
  
  write_to_file(
    head + mid + tail,
    [
      head + mid[0:4],
      mid[4:9],
      tail
    ],
    "should_maintain_order_over_optimal_filling.json"
  )

def write_to_file(input: list[str], expected: list[list[str]], file_name: str):
  with open(f"tests/testdata/{file_name}", "w", encoding="utf-8") as file:
    json.dump(
      {
        "input": input,
        "expected": expected
      }, 
      file, 
      ensure_ascii=False, 
      indent=2
    )

def main():
  generate_should_filter_too_long_ascii_input()
  generate_should_filter_too_long_special_characters_input()
  generate_should_include_1mb_ascii_input()
  generate_should_include_1mb_special_character_input()
  generate_should_maintain_order_over_optimal_filling()

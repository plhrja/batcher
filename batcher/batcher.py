
def batch(
    records: list[str],
    max_record_size: int = 10**6,
    max_batch_size: int = 5 * 10**6,
    max_batch_len: int = 500
) -> list[list[str]]:
  """
  Compiles the records-list into batches. The batch size and length are constrained
  by max_batch_size and max_batch_len. Also, records exceeding the max_record_size 
  are filtered out from the resulting batches.
  
  Args:
    records (list[str]): The records to be batched.
    max_record_size (int): Records larger than this (in bytes) are discarded.
    max_batch_size (int): The max size of a single batch (in bytes).
    max_batch_len (int): The maximum number of records in a single batch.

  Returns:
    list[list[str]]: The original records divided into batches conforming to the above limitations.
  """
  if records is None:
    raise TypeError()
  
  batches = []
  current_batch = []
  current_batch_size = 0
  for record in records:
    record_size = len(record.encode("utf-8"))

    # Discard records exceeding the max allowed size
    if record_size > max_record_size:
      continue
    
    # If adding this record exceeds batch constraints, start a new batch
    if (
      len(current_batch) == max_batch_len 
      or current_batch_size + record_size > max_batch_size
    ):
      batches.append(current_batch)
      current_batch = []
      current_batch_size = 0

    # Add record to the current batch
    current_batch.append(record)
    current_batch_size += record_size
  
  # Append last batch if it has records
  if len(current_batch):
    batches.append(current_batch)
  
  return batches

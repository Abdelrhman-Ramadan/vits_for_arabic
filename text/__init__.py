""" from https://github.com/keithito/tacotron """
# from text import cleaners
from text.symbols import symbols


# Mappings from symbol to numeric ID and vice versa:
_symbol_to_id = {s: i for i, s in enumerate(symbols)}
_id_to_symbol = {i: s for i, s in enumerate(symbols)}

# phoneme_dict = {phone: idx for idx, phone in enumerate(phonemes)}
# vocab = phoneme_dict
# itos = list(vocab.keys())  # Index-to-string mapping
# stoi = vocab  # String-to-index mapping

def text_to_sequence(text, cleaner_names):
  '''Converts a string of text to a sequence of IDs corresponding to the symbols in the text.
    Args:
      text: string to convert to a sequence
      cleaner_names: names of the cleaner functions to run the text through
    Returns:
      List of integers corresponding to the symbols in the text
  '''
  # sequence = []

  # clean_text = _clean_text(text, cleaner_names)
  # for symbol in clean_text:
  #   symbol_id = _symbol_to_id[symbol]
  #   sequence += [symbol_id]
  # return sequence
  return encode(text)

def encode(text):
    # Convert a phoneme sequence into a list of indices
    return [_symbol_to_id[phoneme] for phoneme in text.split() if phoneme in _symbol_to_id]

def decode(tokens):
    # Convert a list of indices back into a phoneme sequence
    return ' '.join([_id_to_symbol[i] for i in tokens if i < len(_id_to_symbol)])

def cleaned_text_to_sequence(cleaned_text):
  '''Converts a string of text to a sequence of IDs corresponding to the symbols in the text.
    Args:
      text: string to convert to a sequence
    Returns:
      List of integers corresponding to the symbols in the text
  '''
  sequence = [_symbol_to_id[symbol] for symbol in cleaned_text]
  return sequence


def sequence_to_text(sequence):
  '''Converts a sequence of IDs back to a string'''
  # result = ''
  # for symbol_id in sequence:
  #   s = _id_to_symbol[symbol_id]
  #   result += s
  # return result
  return decode(sequence)


# def _clean_text(text, cleaner_names):
#   for name in cleaner_names:
#     cleaner = getattr(cleaners, name)
#     if not cleaner:
#       raise Exception('Unknown cleaner: %s' % name)
#     text = cleaner(text)
#   return text

def search4vowels(phrase:str) -> set:
  """Display any vowels found in a supplied word."""
  vogais = set('aeiou')
  return vogais.intersection(set(phrase))



def search4letters(phrase:str, letters:str='aeiou') -> set:
    """Return a set of he 'letters' found in 'phrase' """
    return set(letters).intersection(set(phrase))



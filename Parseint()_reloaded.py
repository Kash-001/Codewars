def parse_int(textnum: str, numwords={}):
    if not numwords:
      decs = [
        "zero", 
        "one", 
        "two", 
        "three", 
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
        "ten",
        "eleven",
        "twelve",
        "thirteen",
        "fourteen",
        "fifteen",
        "sixteen",
        "seventeen",
        "eighteen",
        "nineteen"]
      diz = [
        "",
        "",
        "twenty",
        "thirty",
        "forty",
        "fifty",
        "sixty",
        "seventy",
        "eighty",
        "ninety"]
      th = [
        "hundred",
        "thousand",
        "million"]

      numwords["and"] = (1, 0)
      for index, word in enumerate(decs):
          numwords[word] = (1, index)
      for index, word in enumerate(diz):
          numwords[word] = (1, index * 10)
      for index, word in enumerate(th):
          numwords[word] = (10 ** (index * 3 or 2), 0)

    current = result = 0
    for word in textnum.replace('-',' ').split():
        scale, increment = numwords[word]
        current = current * scale + increment
        if scale > 100:
            result += current
            current = 0

    return result + current

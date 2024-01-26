# Sick of coding w/the book's style? Typing print lines?
# Need a better way? Try triple quotation marks!

# Triple quotes treats multiple str lines as one block,
# *MOSTLY preserving our ASCII whitespace formatting.

# We've two exapmles for this here:
# first, save the strs as a single var (TREE), and print the var;
# second, directly print the str all at once (CAT).

# Draw TREE
tree = """   *
  ***
 *****
*******
  ***
"""
print(tree)


# Draw CAT
print("""
/\\   /\\
  o o
 =   =
  ---""")

# *One note on MOSTLY: On TREE, the quotes catch our initial newline:
# """
#    *
#   ***
#  *****
# and that breaks the lab's expectation.

# To pass, our nice, even whitespacing must be broken instead:
# """    *
#   ***
#  *****

# On the CAT, we've got one free newline left from the TREE print, so
# we can start with a nice newline, preserve the art, and still pass:
# """
# /\\   /\\
#   o o

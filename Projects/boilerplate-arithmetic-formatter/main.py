# This entrypoint file to be used in development. Start by reading README.md
from unittest import main #pytest

from arithmetic_arranger import arithmetic_arranger


print(arithmetic_arranger(['1 + 2', '1 - 9380']))


# Run unit tests automatically
main()

"""
This module lets you practice the ACCUMULATOR pattern
in its simplest classic forms:
   SUMMING:       total = total + number

Authors: David Mutchler, Valerie Galluzzi, Mark Hays, Amanda Stouder,
         their colleagues and Joe Krisciunas.
"""  #


def main():

    """ Calls the   TEST   functions in this module. """

    run_test_sum_cosines()
    run_test_sum_square_roots()


def run_test_sum_cosines():
    """ Tests the   sum_cosines   function. """
    # ------------------------------------------------------------------
    # Done
    #   It TESTS the  sum_cosines  function defined below.
    #   Include at least **   3   ** tests.
    #
    # Use the same 4-step process as in implementing previous
    # TEST functions, including the same way to print expected/actual.
    # ------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Testing the   sum_cosines   function:')
    print('--------------------------------------------------')
 #test 1
    expected1 = 0.13416
    answer1 = sum_cosines(3)
    print('Test 1 expected:', expected1)
    print('         actual:', answer1)

    # test 2
    expected2 = 1.12416
    answer2 = sum_cosines(2)
    print('Test 2 expected:', expected2)
    print('         actual:', answer2)

    # test 3
    expected3 = 1.54030
    answer3 = sum_cosines(1)
    print('Test 3 expected:', expected3)
    print('         actual:', answer3)

def sum_cosines(n):
    import math
    total = 1

    for k in range(n):
        total = total + math.cos(k + 1)

    return total

    """
    What comes in:  A non-negative integer n.
    What goes out:  The sum of the cosines of the integers
       0, 1, 2, 3, ... n, inclusive, for the given n.
    Side effects:   None.
    Example:
      If n is 3, this function returns
        cos(0) + cos(1) + cos(2) + cos(3)   which is about 0.13416.
    """
    # ------------------------------------------------------------------
    # TODO: 3. Implement and test this function(This code works but I think I did it wrong)
    #   Note that you should write its TEST function first (above).
    #   That is called TEST-DRIVEN DEVELOPMENT (TDD).
    #
    #   No fair running the code of  sum_cosines  to GENERATE
    #   test cases; that would defeat the purpose of TESTING!
    # ------------------------------------------------------------------


def run_test_sum_square_roots():
    """ Tests the   sum_square_roots   function. """
    # ------------------------------------------------------------------
    # Done
    #   It TESTS the  sum_square_roots  function defined below.
    #   Include at least **   3   ** tests.
    #
    # Use the same 4-step process as in implementing previous
    # TEST functions, including the same way to print expected/actual.
    # ------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Testing the   sum_square_roots   function:')
    print('--------------------------------------------------')
#test 1
    expected1 = 11.854408
    answer1 = sum_square_roots(5)
    print('Test 1 expected:', expected1)
    print('         actual:', answer1)

    # test 2
    expected2 = 5.8637
    answer2 = sum_square_roots(3)
    print('Test 2 expected:', expected2)
    print('         actual:', answer2)

    # test 3
    expected3 = 19.0602
    answer3 = sum_square_roots(7)
    print('Test 3 expected:', expected3)
    print('         actual:', answer3)

def sum_square_roots(n):


    total = 0

    for k in range(n):
        total = total + (2*(k + 1))**.5

    return total

    """
    What comes in:  A non-negative integer n.
    What goes out:  The sum of the square roots of the integers
       2, 4, 6, 8, ... 2n    inclusive, for the given n.
           So if n is 7, the last term of the sum is
           the square root of 14 (not 7).
    Side effects:   None.
    Example:
      If n is 5, this function returns
         sqrt(2) + sqrt(4) + sqrt(6) + sqrt(8) + sqrt(10),
      which is about 11.854408.
    """
    # ------------------------------------------------------------------
    # Done
    #   Note that you should write its TEST function first (above).
    #   That is called TEST-DRIVEN DEVELOPMENT (TDD).
    #
    #   No fair running the code of  sum_square_roots  to GENERATE
    #   test cases; that would defeat the purpose of TESTING!
    # ------------------------------------------------------------------


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------

main()

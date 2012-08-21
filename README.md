PyConstraints
===

A simple, constraints satisfaction problem solver. Used for the [YACS][] course
scheduler project.

[yacs]: http://github.com/jeffh/yacs

Usage
-----

The Problem is the primary interface:

    >>> from pyconstraints import Problem

And then specify your problem to solve with various constraints:

    >>> p = Problem()
    >>> p.add_variable('x', range(4)) # variable-name, domain
    >>> p.add_variable('y', range(4))
    # give constraint function and list of variables used
    >>> p.add_constraint(lambda x, y: x != y, ['x', 'y'])
    >>> p.add_constraint(lambda x: x % 2 == 0)

Then get your solutions:

    >>> p.get_solutions()
    # => ({'y': 0, 'x': 2},
    #     {'y': 1, 'x': 0},
    #     {'y': 1, 'x': 2},
    #     {'y': 2, 'x': 0},
    #     {'y': 3, 'x': 0},
    #     {'y': 3, 'x': 2})

Or iteratively:

    >>> p.iter_solutions().next()
    # => {'y': 0, 'x': 2}

And that's it!

Using Another Solver
--------------------

Simply pass the solver to the Problem constructor:

    >>> from pyconstraints import BruteForceSolver, BacktrackingSolver
    >>> p = Problem(BacktrackingSolver()) # BruteForceSolver is default

Because the BruteForceSolver uses itertools, there may be cases where it is
faster than the BacktrackingSolver.


Writing Your Own Solver
-----------------------

For convinence, there is a ``pyconstraints.SolverInterface`` Abstract-Base Class if you want to
implement all the features manually:

    @abstractproperty
    def solutions_seen(self):
        "Returns the number of solutions currently seen by the solver."

    @abstractproperty
    def solutions_at_points(self):
        """Returns a dictionary of {iteration_index: solution} of all known
        solutions while iterating.
        """

    @abstractmethod
    def set_conditions(self, variables, constraints):
        """Called by the Problem class to assign the variables and constraints
        for the problem.

            variables = {variable-name: list-of-domain-values}
            constraints = [(constraint_function,
                            variable-names,
                            default-variable-values)]
        """

    @abstractmethod
    def restore_point(self, starting_point=None):
        "Restores the iteration state to a given starting point."

    @abstractmethod
    def save_point(self):
        """Returns data to indicate a way to restore to the current iteration
        point.
        """

    @abstractmethod
    def __iter__(self):
        "Yields solutions."

But for convinence, you can inherit from the ``pyconstraints.SolverBase`` class
which provides a primitive implementation for all the interface methods except
for ``__iter__`` and ``set_conditions``.


Todo
-----

- Speed up backtracking solver
- Add more solvers?

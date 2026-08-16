# MapReduce Mutual Friends

This project implements a MapReduce-style solution to compute mutual friends in a social graph and compares the performance of:

- a single-process implementation
- a multi-processing implementation

## Project goal

The main objective is to demonstrate how a MapReduce workflow can be implemented in Python and how multiprocessing can speed up the processing of larger datasets.

Given a friend list such as:

- Alice -> [Ben, Carol, Cleo, Ivan, Karl, Nina, Uma]
- Dave -> [Amy, Ivan, Judy, Karl, Oscar, Uma]

The program identifies common friends between two names.

Example:

- Alice and Dave share: Ivan, Karl, Uma

## How it works

The program:

1. Builds a friend graph from the dataset.
2. Creates all unique pairs of friends in each person's list.
3. Groups those pairs using a MapReduce-style flow.
4. Uses multiprocessing to parallelize the map and reduce stages.
5. Compares the result with a single-process version.
6. Looks up the mutual friends for a given pair of names.

## Performance comparison

The script measures and prints two timings at startup:

- Single-core MapReduce build time
- Multi-processing MapReduce build time

This makes it easy to compare the runtime of the same MapReduce pipeline when it is run with one process versus multiple worker processes.

The multiprocessing version is useful for larger datasets because it distributes chunks of the input across workers and combines the results afterward.

## Run the project

From the project directory:

```bash
python mapreduce.py
```

## Example usage

```text
MapReduce build time(Single-core): 0.142625 seconds
MapReduce build time (Multi-processing): 0.082421 seconds
Enter two friends: alice DAVE
Mutual friends: (3) : ivan,karl,uma
Enter two friends: exit
Goodbye!
```

## Notes

- The program accepts two names separated by a space.
- It loops until the user enters `exit`.
- The output is case-insensitive for the names, but the final printed names may be shown in lowercase depending on the current implementation.

## Files

- `mapreduce.py` — main implementation
- `.gitignore` — ignores Python cache and local editor files
- `README.md` — project documentation

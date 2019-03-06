# hids_thesis

## Goal

This project has the following goal:

`Building of an HIDS that detects unauthorized or unusual behaviour on the file system. Compared to traditional HIDS file system integrity checking, it should scale with a lot of data and have the possibility to be used for investigation (retain historic data) built in from the start.`

### Subgoals

Searching
  Can search FS using sleuthkit
  Can analyze the results of sleuthkit
Differences
  Can find differences
Recording
  Records analyzed files
  Records differences

Evaluation
  Can find annomalies automatically (optional? machine learning)
  Can evaluate files based on rules
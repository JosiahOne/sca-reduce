# sca-reduce

A distributed, static code analysis tool used for finding flaws in various programming languages that directly affect security.

This is a mapreduce procedure which presently checks for:

* Dangerous C and C++ functions.

## To Run

1) Install hadoop and java.
1.1) On macOS this means: brew cask install java; brew install hadoop;
2) Place source in a flat stucture in hadoop/input
3) Run ./bin/hadoop_pipeline

That's it. Output will be dumped to hadoop/output

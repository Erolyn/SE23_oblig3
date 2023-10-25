# oblig3

Initially I created .github/workflow-structure, with the corresponding YML-file.

I received a few errors, the first related to test_leap_year not finding the leap_year-module.
After some going back and forth, which included changing pathing, the problem was resolved. 
Also needed to add init-files to both modules to make the tests run.

Further testing of actions with the new change in node.js-versions, didn't quite succesfully remove the warnings. 
However, the tests run smoothly and all tests pass after each commit. Also tested to make sure it would fail if one of the tests failed.
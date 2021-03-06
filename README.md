# dev-nekoboi's Python Module
A miscellaneous Python module for all of the functions that I wish were Python features.

---

Contact information:
---

To report any bugs that you find, please email [dev@nekoboi.com](mailto:dev@nekoboi.com) with the subject line `github:dn-py-misc:bugs`.

To submit a suggestion for a function to add to the module, please email [dev@nekoboi.com](mailto:dev@nekoboi.com) with the subject line: `github:dn-py-misc:suggestion`.

For any other topic related to this repository and the module packaged within, please email [dev@nekoboi.com](mailto:dev@nekoboi.com) with the subject line: `github:dn-py-misc:misc`.

---

Documentation:
---

```python
prompt(out, condition, err, transform)
```
This function prompts the user to enter an input. `out` is an optional parameter which should be the output value to prompt the user with. `condition` is an optional parameter which, if supplied, should be a funciton which takes in a single input and outputs a boolean. If a condition is supplied, then the user's input **must** meet that condition before it is returned. The user will continue to be prompted until they provide a valid input. `err` is an optional parameter which will be printed in the case that the input which the user provides should not meet the condition supplied. If no condition is supplied, `err` will never be printed and it can therefore be left blank. `transform` is an optional parameter which, if supplied, should be a function that takes a single input and provides an output. If a transform is supplied, the user's input will be passed through said transform before the value of that input is returned from the `prompt()` function.

---

```python
canBe(val, type)
```
This function will return a boolean value of `True` if `val` is an instance of `type` _or_ if `val` can be successfully converted _into_ an instance of `type`, and `False` otherwise. Both parameters are required.

Note: if converting `val` to an instance of `type` via `type(val)` does not produce the `ValueError` exception, and `val` is not already an instance of `type`, the function _will_ return `True`. Consider this carefully when designing constructors for custom types, as it has the potential to cause runtime errors.

---

```python
root(base, index)
```
This function will return `base` to the `index`th root. The `base` parameter is required. The `index` parameter is optional, and will default to `2`.

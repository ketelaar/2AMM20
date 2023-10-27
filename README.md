# 2AMM20 Code

## Duplication of the Mushrooms Dataset
**Note: This file was tested with Python 3.11.4 and pandas 2.1.1. Pandas is the only Python dependency that is required for this script**

``duplicate.py`` is used to duplicate the mushrooms dataset. In order to do this follow these steps:

1. Download and extract the mushroom dataset, which can be retrieved from https://archive.ics.uci.edu/dataset/73/mushroom.
2. Place ``duplicate.py`` in the same folder as ``agaricus-lepiota.data``, which was extracted from the ``.zip`` file in the previous step.

Now for execution enter the following in your terminal (either ``powershell``, ``bash``, ``zsh`` or any other, depends on your operating system):
```
python duplicate.py duplication_factor
```
Where ``duplication_factor`` is the number you wish to duplicate the dataset by.

**For example**, if you choose ``1000`` for your ``duplication_factor``, you enter:
```
python duplicate.py 1000
```
This will produce the file ``mushrooms-1000.csv``, which is the mushrooms dataset duplicated a 1000 times.

## Execution of PySubgroup, Subgroups and RSubgroup
Subgroup Discovery can be done by ``PySubgroup`` by executing ``main.py`` (found in the ``pysubgroup`` directory). Python of at least version 3.6 is needed to run this process.

Subgroup Discovery can be done by ``Subgroups`` by executing ``main2.py`` (found in the ``subgroups`` directory). Python of at least version 3.9 is needed to run this process.

Subgroup Discovery can be done by ``RSubgroup`` by executing ``main.r`` (found in the ``rsubgroup`` directory). R of at least version 2.10 and Java at least version 8 are both needed to run this process.


# threads using conditional variables

Simple multiple thread producer/consumer in python 
- To run: python main.py

- producer an an item at most one per second. Consumer consumes as fast as possible
- using conditonal variable. You cannot check lock status. Also you can only notify() while holding the lock
-- acquire(), release(), notify() or notify\_all()


## My Projects
  
Here is some more detailed in formation about projects I have done within two years.

* Python Examples - I do not consider myself a programmer; I create these little programs as experiments to have a play with the language. I would gladly accept pointers from others to improve the code and make it more efficient, or simplify the code. If you would like to make any comments then please feel free to email me at techjennifer@gmail.com.
- [create_flight_schedule.py] ()
  - Scenario
  A new startup airline is needing help with creating and optimizing a flight schedule. They have hired you as a
  data scientist to create and optimize a flight schedule. The airlines will be all business class and cater to
  business travel. All aircraft are configured exactly the same and can fly any route in the system interchangeably.
  The airline will serve Dallas Love Field (DAL), Austin Bergstrom (AUS), and Houston Hobby (HOU). 
  - Aircraft and Tail Numbers
  There are 6 aircraft. Tail numbers: T1, T2, T3, T4, T5, T6
  - Restrictions
  flights cannot have a departure time of 0559 or earlier
  flights can have a departure time of exactly 06:00
  flights can have an arrival time of exactly 22:00
  flights cannot have an arrival time of 2201 or later
  - Flight Times
  AUS <-> DAL 50 minutes
  AUS <-> HOU 45 minutes
  DAL <-> HOU 65 minutes
  - Number of Gates and Minimim Ground Time at Airport
  AUS has 1 gates, ground time is 25 minutes 
  DAL has 2 gates, ground time is 30 minutes
  HOU has 3 gates, ground time is 35 minutes
  - Optimization Goals
  Our optimization goals are to maximize the number of flights, utilize aircraft as evenly as possible, 
  and utilize gates at airports as evenly as possible, and distribute flights among all 6 markets.

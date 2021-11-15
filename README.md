# WhiteBoxTestingGame
## Members

- Daniel Camacho
- Juan Jose Quiroga
- Allen Vargas

## 1. Describing the Exercise
In this practice we are testing a software that was developed by Juan Jose Quiroga in the assignature of "Sistemas Inteligentes". The goal of this practice is make unit testing, for  try to cover as much coverage as possible. The project that we are testing is the classic game of the river crossing, in this game instead of having wolfs we have executioners and instead of have sheeps we have Mapuches as it can see in the first ficture
![game](https://github.com/Gestion-de-Calidad-2021/WhiteBoxTestingGame/blob/master/readmeImages/juego.jpg)

In the way to test the code and increase the coverage we start getting the initial coverage in the code for do that we install Pytest and coverage that are complement librarys for unit test, the results are the next one
![coverage](https://github.com/Gestion-de-Calidad-2021/WhiteBoxTestingGame/blob/master/readmeImages/coverage%2008.11.21.jpg)
## 2. Results

After doing the unit tests to the most part of the code we have the next results:

![finalCoverage](https://github.com/Gestion-de-Calidad-2021/WhiteBoxTestingGame/blob/master/readmeImages/final_coverage.png)

We test all the classes but the main.py because we just want to test all the funtionallity and dont want to test the unification because it have visual functionallitys that dont are the goal of this practice they are more visual task taht can be testing with black box tests, all the classes has his test in the files that has the same name but with a "test_" ahead.

## 3. Conclusions

We achieve the main goal and we cover the 100% in the fields that we want.
## 4. Installation guide
To get start the installation guide we just have to have installed python.
- The fist step is install the pygame libray in order to run the code we do that in anaconda cmd or in your cmd with the next comand:

    - pip install pygame 
- The second step is install all the library for do the unit test and coverage the code, so we open the anaconda/local cmd and enter the next command:

    - pip install unittest
    - pip install pytest
    - pip install coverage
    - pip install pytest-cov

When we do all that we are ready to test the app with his own commands, the command that we used to get the report of the coverage in the console and also in a html page is:

    - python -m pytest -v --cov  --cov-report=html 

## 5. Bibliography

➡️  Documentation: [Practica 3 Informe][Documentation]

➡️  PyGame: [PyGame installation][pyGame]

➡️  Installation Guide Video: [PyGame installation][Installation_Guide]

➡️  Related Games: [River Crossing games][river]

[Documentation]: https://docs.google.com/document/d/1Hr20V0DZpghZsD-QDwmHQrNLPcIB2Po0wkp7MxFP_E4/edit?usp=sharing

[pyGame]: https://www.pygame.org/news

[Installation_Guide]: https://www.youtube.com/watch?v=7BJ_BKeeJyM

[river]: https://www.transum.org/software/River_Crossing/


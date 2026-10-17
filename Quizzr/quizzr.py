def assign_grade(score):
    if 90 <= score <= 100:
        return "A"
    elif 80 <= score < 90:
        return "B"
    elif 70 <= score < 80:
        return "C"
    elif 60 <= score < 70:
        return "D"
    else:
        return "F"
def quiz(subject_name, questions, answers, correct_answers, username):
    score = 0

    for question_num in range(10):
        print("--------------------")
        print(questions[question_num])
        for option in answers[question_num]:
            print(option, end=" ")
        print()
        while True:
            guess = input("Enter Your Answer (A, B, C OR D): ")
            guess = guess.upper()
            if guess in ["A", "B", "C", "D"]:
                break
            else:
                print("Enter a Valid Choice (A, B, C OR D)")
        if guess == correct_answers[question_num]:
            score += 1

    percentage = score * 10
    grade = assign_grade(percentage)
    print("---------------------")
    print("---FINAL SCORECARD---")
    print("---------------------")
    print(f"Name: {username}")
    print(f"Subject: {subject_name}")
    print(f"Score: {score}")
    print(f"Percentage: {percentage}")
    print(f"Grade: {grade}")
#GK
questions_gk = ("1. Which is the largest continent by area?",
                "2. Which is the tallest mountain peak in the world?",
                "3. What country gifted the State of Liberty to the USA?",
                "4. Which is the smallest planet in the solar system?",
                "5. How many continents are there on Earth?",
                "6. What is the capital of Australia?",
                "7. What is the process through which green plants make food?",
                "8. What is the most abundant gas in the Earth's atmosphere?",
                "9. Which is the longest river in the world?",
                "10. Which animal has blue blood?")
answers_gk = (("A. Africa", "B. Europe", "C. Asia", "D. Antarctica"),
              ("A. K2", "B. Mount Everst", "C. Kanchenjunga", "D. Lhotse"),
              ("A. Spain", "B. Italy", "C. England", "D. France"),
              ("A. Venus", "B. Mars", "C. Mercury", "D. Earth"),
              ("A. 5", "B. 6", "C. 7", "D. 8"),
              ("A. Sydney", "B. Canberra", "C. Melbourne", "D. Perth"),
              ("A. Respiration", "B. Transpiration", "C. Fermentation", "D. Photosynthesis"),
              ("A. Oxygen", "B. Nitrogen", "C. Carbon Dioxide", "D. Hydrogen"),
              ("A. Amazon", "B. Ganges", "C. Yangtze", "D. Nile"),
              ("A. Octopus", "B. Blue Whale", "C. Jellyfish", "D. Starfish"))
correct_answers_gk = ("C", "B", "D", "C", "C", "B", "D", "B", "D", "A")

#MATHS
questions_maths = ("1. What is the cube root of 1331?",
                   "2. What is the square root of 144?",
                   "3. What is 15% of 200?",
                   "4. Solve for x: 2x + 5 = 15",
                   "5. What is the value of pi (upto 2 decimal places)?",
                   "6. What is the sum of angles in a triangle (in degrees)?",
                   "7. What is the derivative of x^2",
                   "8. If a train travels 60km in 1.5 hours, what is its speed in km/hr?",
                   "9. What is the value of log base 10 of 1000?",
                   "10. Solve: If roots of x^2-5x+6 = 0 are a and b, what is a + b?")
answers_maths = (("A. 17", "B. 16", "C. 11", "D. 13"),
                ("A. 10", "B. 11", "C. 12", "D. 14"),
                ("A. 25", "B. 20", "C. 30", "D. 35"),
                ("A. 3", "B. 5", "C. 7", "D. 10"),
                ("A. 3.14", "B. 3.12", "C. 3.16", "D. 3.18"),
                ("A. 90", "B. 180", "C. 270", "D. 45"),
                ("A. x", "B. 2x", "C. 0", "D. 2"),
                ("A. 30", "B. 50", "C. 45", "D. 40"),
                ("A. 2", "B. 3", "C. 4", "D. 10"),
                ("A. 5", "B. 6", "C. -5", "D. 1"))
correct_answers_maths = ("C", "C", "C", "B", "A", "B", "B", "D", "B", "A")
#PHYSICS
questions_physics = ("1. What is the SI unit of force?",
                     "2. Who proposed the three laws of motion?",
                     "3. What is the negatively charged subatomic particle known as?",
                     "4. What physical quantitiy has SI unit Pascal",
                     "5. What type of lens is used to correct myopia (short sightedness)?",
                     "6. What is the SI unit of electric current?",
                     "7. A force of 10N acts on a 2kg mass. What is the acceleration produced (in SI unit)?",
                     "8. Which form of energy is possessed by a body due to its motion?",
                     "9. What is the phenomenon called when light bends while passing from one medium to another?",
                     "10. A car moving at 20 m/s comes to rest in 4 seconds. What is its deceleration (in SI unit)?")
answers_physics = (("A. Joule", "B. Newton", "C. Watt", "D. Pascal"),
                ("A. Einstein", "B. Galileo", "C. Newton", "D. Kepler"),
                ("A. Neutron", "B. Proton", "C. Electron", "D. Quarks"),
                ("A. Energy", "B. Potential", "C. Pressure", "D. Force"),
                ("A. Convex lens", "B. Concave lens", "C. Cylindrical lens", "D. Bifocal lens"),
                ("A. Volt", "B. Ohm", "C. Ampere", "D. Watt"),
                ("A. 2", "B. 5", "C. 10", "D. 20"),
                ("A. Potential energy", "B. Kinetic energy", "C. Thermal energy", "D. Chemical energy"),
                ("A. Reflection", "B. Diffraction", "C. Refraction", "D. Dispersion"),
                ("A. 5", "B. 4", "C. 2", "D. 8"))
correct_answers_physics = ("B", "C", "C", "C", "B", "C", "B", "B", "C", "A")

#CHEMISTRY
questions_chemistry = ("1. What is the chemical symbol for gold?",
                       "2. Which gas is released when metals react with acids?",
                       "3. What is the pH value of a neutral solution?",
                       "4. Which element has atomic number 10?",
                       "5. What is the common name for sodium chloride?",
                       "6. Which gas do plants absorb during photosynthesis?",
                       "7. What type of bond is formed by sharing of electrons?",
                       "8. Which particle in an atom carries a negative charge?",
                       "9. What is the process of a solid turning directly into a gas called?",
                       "10. Which gas makes up majority of Earth's atmosphere?")
answers_chemistry = (("A. G", "B. Au", "C. Go", "D. Ag"),
                    ("A. Oxygen", "B. Carbon Dioxide", "C. Hydrogen", "D. Smoke"),
                    ("A. <7", "B. >7", "C. 0", "D.7 "),
                    ("A. Sodium", "B. Neon", "C. Oxygen", "D. Carbon"),
                    ("A. Common salt", "B. Baking soda", "C. Chalk", "D. Vinegar"),
                    ("A. Oxygen", "B. Carbon Dioxide", "C. Nitrogen", "D. Hydrogen"),
                    ("A. Ionic bond", "B. Metallic bond", "C. Coordinate bond", "D. Covalent bond"),
                    ("A. ELectron", "B. Proton", "C. Neutron", "D. Nucleus"),
                    ("A. Evaporation", "B. Deposition", "C. Sublimation", "D. Antifreezing"),
                    ("A. Oxygen", "B. Carbon Dioxide", "C. Nitrogen", "D. Hydrogen"))
correct_answers_chemistry = ("B", "C", "D", "B", "A", "B", "D", "A", "C", "C")

#BIOLOGY
questions_biology = ("What is the powerhouse of a cell?",
                     "Which blood cells help fight infection?",
                     "What is the basic unit of heredity called?",
                     "Which organ pumps blood throughout the human body?",
                     "What is the process by which plants lose water through leaves called?",
                     "Which gas do humans exhale during respiration?",
                     "What is the largest organ in the human body?",
                     "Which part of the plant conducts photosynthesis?",
                     "What is the structure of DNA?",
                     "How many chambers does the human heart have?")
answers_biology = (("A. Nucleus", "B. Ribosome", "C. Golgi body", "D. Mitochondria"),
                  ("A. White blood cells", "B. Red blood cells", "C. Platelets", "D. Plasma"),
                  ("A. Cell", "B. Chromosome", "C. Protein", "D. Gene"),
                  ("A. Lungs", "B. Brain", "C. Heart", "D. Kidney"),
                  ("A. Photosynthesis", "B. Transpiration", "C. Respiration", "D. Germination"),
                  ("A. Oxygen", "B. Carbon Dioxide", "C. Nitrogen", "D. Hydrogen"),
                  ("A. Liver", "B. Brain", "C. Heart", "D. Skin"),
                  ("A. Root", "B. Stem", "C. Flower", "D. Leaf"),
                  ("A. Spherical", "B. Linear", "C. Double Helix", "D. Amoeboid"),
                  ("A. 2", "B. 3", "C. 4", "D. 5"))
correct_answers_biology = ("D", "A", "D", "C", "B", "B", "D", "D", "C", "C")

username = input("Enter your Name: ")
print("SUBJECT LIST:")
print("1. General Knowledge")
print("2. Mathematics")
print("3. Physics")
print("4. Chemistry")
print("5. Biology")
while True:
    try:
        choice = int(input("Enter Subject Number: "))
        if 1 <= choice <= 5:
            break
        else:
            print("Enter a Number between 1 and 5")
    except ValueError:
        print("Invalid Input. Enter a Number between 1 and 5")
if choice == 1:
    quiz("General Knowledge", questions_gk, answers_gk, correct_answers_gk, username)
elif choice == 2:
    quiz("Maths", questions_maths, answers_maths, correct_answers_maths, username)
elif choice == 3:
    quiz("Physics", questions_physics, answers_physics, correct_answers_physics, username)
elif choice == 4:
    quiz("Chemistry", questions_chemistry, answers_chemistry, correct_answers_chemistry, username)
elif choice == 5:
    quiz("Biology", questions_biology, answers_biology, correct_answers_biology, username)
print("Thank You for Using this Program!")

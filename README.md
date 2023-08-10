# Tema3_laborator_LFA

## Automatul minimal


Input: un AFD complet

Exemple de AFD-uri complete:

![image](https://github.com/teodorma/Tema3_laborator_LFA/assets/108132918/66454f48-91a4-44c8-a42e-dc873f78cc8b)

    q0 0 q1
    q0 1 q2
    q1 0 q0
    q1 1 q3
    q2 0 q5
    q2 1 q4
    q3 0 q5
    q3 1 q4
    q4 0 q4
    q4 1 q4
    q5 0 q5
    q5 1 q4
    q5


![image](https://github.com/teodorma/Tema3_laborator_LFA/assets/108132918/32661430-c792-4982-94fc-93ccd56c9578)

    q0 a q1
    q0 b q3
    q1 a q0
    q1 b q3
    q2 a q1
    q2 b q4
    q3 a q5
    q3 b q5
    q4 a q3
    q4 b q3
    q5 a q5
    q5 b q5
    q3 q5

Output: AFD-ul minimal rezultat in urma aplicarii algoritmului de minimizare asupra automatului dat ca input

Automatele date mai sus dupa minimizare:

![image](https://github.com/teodorma/Tema3_laborator_LFA/assets/108132918/b5d2ac0e-f371-455b-b007-2a613a54a6d4)


![image](https://github.com/teodorma/Tema3_laborator_LFA/assets/108132918/04808349-7ae8-4a7d-ab23-9c73bcc45e4e)

Resurse: 
- https://www.geeksforgeeks.org/minimization-of-dfa/
- https://www.javatpoint.com/minimization-of-dfa

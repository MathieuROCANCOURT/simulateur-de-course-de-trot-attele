# Simulateur de course de trot attelé

Une course de trot attelé rassemble 12 à 20 chevaux. Elle peut faire l’objet d’un tiercé, d’un quarté, ou d’un quinté.
La course se déroule sur un hippodrome, d’une longueur de 2400m. Il est à noter que chaque cheval doit respecter
l’allure du trot de bout en bout, le passage au galop entrainant sa disqualification.

## Déroulement de chaque tour de jeu

Un tour de jeu représente 10" de course. Chaque tour, on lance un dé qui est entre 1 et 6. En fonction de la vitesse
actuelle du cheval et du jet de dé, la vitesse de ce tour va augmenter, rester stable ou diminuer et dans un cas, que le
cheval soit disqualifié pour avoir était trop vite.

Voici le tableau qui indique les évolutions de la vitesse d'un cheval en fonction de sa vitesse actuelle et du jet de
dé.


<table style="border-collapse: collapse;">
    <tr>
        <td></td>
        <td></td>
        <th colspan="6" style="background-color: lightcyan">Jet de dé</th>
    </tr>
    <tr>
        <td></td>
        <td></td>
        <td>1</td>
        <td>2</td>
        <td>3</td>
        <td>4</td>
        <td>5</td>
        <td>6</td>
    </tr>
    <tr>
        <th rowspan="7" style="background-color: lightcyan;">
            <div style="transform: rotate(-90deg); white-space: nowrap">
                Vitesse actuelle
            </div>
        </th>
        <td>0</td>
        <td>0</td>
        <td>+1</td>
        <td>+1</td>
        <td>+1</td>
        <td>+2</td>
        <td>+2</td>
    </tr>
    <tr>
        <td>1</td>
        <td>0</td>
        <td>0</td>
        <td>+1</td>
        <td>+1</td>
        <td>+1</td>
        <td>+2</td>
    </tr>
    <tr>
        <td>2</td>
        <td>0</td>
        <td>0</td>
        <td>+1</td>
        <td>+1</td>
        <td>+1</td>
        <td>+2</td>
    </tr>
    <tr>
        <td>3</td>
        <td>-1</td>
        <td>0</td>
        <td>0</td>
        <td>+1</td>
        <td>+1</td>
        <td>+1</td>
    </tr>
    <tr>
        <td>4</td>
        <td>-1</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>+1</td>
        <td>+1</td>
    </tr>
    <tr>
        <td>5</td>
        <td>-2</td>
        <td>-1</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>+1</td>
    </tr>
    <tr>
        <td>6</td>
        <td>-2</td>
        <td>-1</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>D</td>
    </tr>

</table>

De même, voici le tableau qui permet la distance parcourue en 10" en fonction de la vitesse à avancer du cheval.

<table style="border-collapse: collapse;">
    <tr>
        <td></td>
        <td></td>
        <th colspan="6" style="background-color: lightcyan">Jet de dé</th>
    </tr>
    <tr>
        <td></td>
        <td>0</td>
        <td>1</td>
        <td>2</td>
        <td>3</td>
        <td>4</td>
        <td>5</td>
        <td>6</td>
    </tr>
    <tr>
        <th style="background-color: lightcyan">Distance (m)</th>
        <td>0</td>
        <td>23</td>
        <td>46</td>
        <td>69</td>
        <td>92</td>
        <td>115</td>
        <td>138</td>
    </tr>
</table>
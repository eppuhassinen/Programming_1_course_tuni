"""
Ohjelmointi 1 / Programming 1
Paracetamol/Panadol/Tylenol Dosing Advisor
Eppu Hassinen
Opiskelijanumero: 50044786
"""


def calculate_dose(weight, time, total_dose):
    """

    :param weight: patietnts weight in kg
    :param time: time from the last dose
    :param total_dose: amount taken in the previous 24 hours
    :return: amount to take
    """

    time_from_prevous_dose: int = 6
    mg_per_kg: int = 15
    max_dose = weight * mg_per_kg
    max_dose_24: int = 4000

    if time < time_from_prevous_dose:
        return 0

    if total_dose >= max_dose_24:
        return 0

    if total_dose + max_dose > max_dose_24:
        return max_dose_24 - total_dose

    return max_dose


def main():

    weight = int(input("Patient's weight (kg): "))
    time = int(input("How much time has passed from"
                     " the previous dose (full hours): "))
    total_dose = int(input("The total dose for the last 24 hours (mg): "))

    print("The amount of Parasetamol to give to the patient:",
          calculate_dose(weight, time, total_dose))

    # calculate_dose assumes parameters to be of type int
    # and they should be passed in the order: weight, time, total_doze_24
    # (or more like the automated tests assume this)


if __name__ == "__main__":
    main()

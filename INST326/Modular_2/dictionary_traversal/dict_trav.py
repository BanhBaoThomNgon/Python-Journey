from energy import energy_2009
def highest_energy(dictionary):
    states = []
    solar = []
    wind = []

    for s_name, s_data in dictionary.items():
        states.append(s_name)
        for key in s_data:
            solar.append(s_data['solar'])
            wind.append(s_data['wind'])
            break

    print("Highest solar power:", max(solar), states[solar.index(max(solar))])
    print("Highest wind power:", max(wind), states[wind.index(max(wind))])

highest_energy(energy_2009)
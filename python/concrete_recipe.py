def sacas_de_cimento_por_metro(proporcao_cimento, peso_saca, densidade_agua=1000):
    # Calcula a quantidade de cimento em quilogramas por metro cúbico
    qtd_cimento_kg = proporcao_cimento * peso_saca

    # Calcula a quantidade de cimento em sacas por metro cúbico
    qtd_cimento_sacas = qtd_cimento_kg / peso_saca

    # Ajusta a quantidade de cimento pela densidade da água (opcional)
    qtd_cimento_sacas = qtd_cimento_sacas * densidade_agua / 1000

    return qtd_cimento_sacas

def concrete():
    # Get input from user
    weight_per_bag = float(input("Enter the weight per bag of cement in kg: "))
    num_bags = int(input("Enter the number of cement bags: "))

    # Calculate material weights
    cement_weight = weight_per_bag * num_bags
    sand_weight = cement_weight * 2
    stone_weight = cement_weight * 4
    water_liters = cement_weight * 0.5

    # Calculate volume of concrete
    density = 2400 # kg/m³
    volume = (cement_weight + sand_weight + stone_weight) / density

    # Calculate total area
    cement_coverage = 0.025 # assume 25 kg of cement covers 1 sqm
    total_area = cement_weight / cement_coverage

    # Calculate number of cement bags needed
    proporcao_cimento = 1  # assumindo a proporção 1:2:3
    peso_saca = 25  # peso padrão de uma saca de cimento
    sacas_necessarias = sacas_de_cimento_por_metro(proporcao_cimento, peso_saca)
    sacas_necessarias *= volume  # ajusta a quantidade de sacas para o volume desejado

    # Print results
    print(f"Total weight of cement: {cement_weight} kg")
    print(f"Total weight of sand: {sand_weight} kg")
    print(f"Total weight of stone: {stone_weight} kg")
    print(f"Total liters of water: {water_liters} L")
    print(f"Total volume of concrete: {volume:.2f} m³")
    print(f"Total area covered: {total_area:.2f} sqm")
    print(f"Number of cement bags needed: {sacas_necessarias:.2f}")

    # Print size of concrete
    side_length = (volume / 2) ** (1/3) # Assuming the concrete is a cube
    print(f"Size of concrete: {side_length:.2f} m x {side_length:.2f} m x {side_length:.2f} m")

concrete()

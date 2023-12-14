import numpy as np

def simulate_proposals(N, n69, n230, n500, c69, c230, c500, pMin, pMax, sPrazo, sPadr, mReserva, sReserva):
    # Define os pesos AHP para as categorias
    ahp_weights = [0.40, 0.17, 0.43]

    # Inicializa a lista de propostas
    proposals = []

    for _ in range(N):
        # Gera valores aleatórios para os subcritérios
        technical_relevance = np.random.choice([0, 10], size=10)
        cost_reasonability = np.random.choice([0, 10], size=2)
        execution_risk = np.random.choice([0, 10], size=3)

        # Calcula o valor da proposta
        costs = np.random.normal([c69, c230, c500], [c69 * sPadr, c230 * sPadr, c500 * sPadr])
        total_cost = np.sum([n69 * costs[0], n230 * costs[1], n500 * costs[2]])

        # Calcula a reserva de emergência
        reserve = np.random.normal(mReserva, sReserva) * total_cost

        # Valor final da proposta
        final_value = total_cost + reserve

        # Valor dos sobressalentes é 10% do valor total
        spare_value = total_cost * 0.1

        # Prazo de instalação
        installation_time = np.random.normal((pMin + pMax) / 2, sPrazo)

        # Calcula as médias para as categorias
        avg_technical_relevance = np.mean(technical_relevance)
        avg_cost_reasonability = np.mean(cost_reasonability)
        avg_execution_risk = np.mean(execution_risk)

        # Calcula o score final com os pesos AHP
        final_score = (avg_technical_relevance * ahp_weights[0] +
                       avg_cost_reasonability * ahp_weights[1] +
                       avg_execution_risk * ahp_weights[2])

        # Adiciona a proposta à lista
        proposal = {
            'technical_relevance': technical_relevance.tolist(),
            'cost_reasonability': cost_reasonability.tolist(),
            'execution_risk': execution_risk.tolist(),
            'total_cost': total_cost,
            'reserve': reserve,
            'final_value': final_value,
            'spare_value': spare_value,
            'installation_time': installation_time,
            'final_score': final_score
        }
        proposals.append(proposal)

    return proposals


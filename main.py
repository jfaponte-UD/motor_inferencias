from src.Entity.Graph import Graph

if __name__ == '__main__':
    graph = Graph()

    hypothesis_a = graph.add_node("A", "True")
    hypothesis_b = graph.add_node("B", "True")
    hypothesis_c = graph.add_node("C", "True")

    hypothesis_g = graph.add_node("G", "True")
    hypothesis_j = graph.add_node("J", "True")

    # rule 1.
    hypothesis_d = graph.add_node("D", "True")
    condition_1 = graph.add_edge(hypothesis_a, hypothesis_d, "Y")

    # rule 2.
    hypothesis_f = graph.add_node("F", "True")
    condition_2 = graph.add_edge(hypothesis_d, hypothesis_f, "Y")
    condition_3 = graph.add_edge(hypothesis_b, hypothesis_f, "Y")

    # rule 3.
    hypothesis_h = graph.add_node("H", "True")
    condition_4 = graph.add_edge(hypothesis_f, hypothesis_h, "Y")
    condition_5 = graph.add_edge(hypothesis_g, hypothesis_h, "Y")

    # rule 4.
    hypothesis_i = graph.add_node("I", "True")
    condition_6 = graph.add_edge(hypothesis_c, hypothesis_i, "Y")

    # rule 5.
    hypothesis_w = graph.add_node("W", "True")
    condition_7 = graph.add_edge(hypothesis_h, hypothesis_w, "Y")
    condition_8 = graph.add_edge(hypothesis_i, hypothesis_w, "Y")

    # rule 6
    # condition_7 = graph.add_edge(hypothesis_h, hypothesis_w, "Y")
    condition_9 = graph.add_edge(hypothesis_j, hypothesis_w, "Y")

    # rule 7
    condition_10 = graph.add_edge(hypothesis_b, hypothesis_g, "Y")

    goal_node = hypothesis_w
    backward_result = graph.backward_chaining(goal_node)
    print("\n\nNodos que satisfacen las condiciones para que el nodo objetivo sea verdadero:")
    for node in backward_result:
        print(f"[Attribute: {node.attribute}, Value: {node.value}]", end=" -> \n")


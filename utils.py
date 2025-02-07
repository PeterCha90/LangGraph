
def check_state(graph, config):
    for state in graph.get_state_history(config):
        messages = state.values["messages"]
        
        if len(messages) > 0:
            print(state.values["messages"][-1].id)
            # 메시지 수 및 다음 상태 출력
            print("메시지 수: ", len(state.values["messages"]), "다음 노드: ", state.next)
            print("-" * 80)
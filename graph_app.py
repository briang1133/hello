# Import necessary libraries
import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt

# Function to create a sample graph
def create_sample_graph():
    G = nx.Graph()
    G.add_edges_from([(1, 2), (1, 3), (2, 4), (2, 5), (3, 6)])
    return G

# Function to draw the graph using Matplotlib
def draw_graph(graph):
    pos = nx.spring_layout(graph)
    nx.draw(graph, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', font_size=8, font_color='black', edge_color='gray')
    plt.title("Graph Visualization")
    return plt

# Streamlit application
def main():
    st.title("Graph Visualization App")

    # Create a sample graph
    graph = create_sample_graph()

    # Draw the graph
    plt = draw_graph(graph)

    # Display the graph only if it has been drawn
    if plt:
        st.pyplot(plt)

# Run the Streamlit app
if __name__ == "__main__":
    main()

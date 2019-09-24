# usually you would pull this from a database but we'll hardcode some data
cell_data = {
    "1": {
        "name": "CA1 pyramidal neuron",
        "location": "brain",
        "role": "learning and memory"
    },
    "2": {
        "name": "Cardiac purkinje cell",
        "location": "heart",
        "role": "propagate contraction signals"
    },
    "3": {
        "name": "Pancreatic beta cell",
        "location": "pancreas",
        "role": "synthesize and secrete insulin"
    }
}


class Model:
    def get_cells():
        return [id_ for id_ in cell_data]
    def get_cell(id_):
        return cell_data.get(id_)

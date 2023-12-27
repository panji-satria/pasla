# eksekusi_model.py
from core.model_training import train_model
from core.tensor_operations import perform_tensor_operation

def execute_model(data, labels):
    trained_model = train_model(data, labels)

    result = perform_tensor_operation(data)

    print(f"Execution result: {result}")

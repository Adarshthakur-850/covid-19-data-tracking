from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
import os
from .config import MODELS_DIR, BATCH_SIZE, EPOCHS, PATIENCE

def train_model(model, X_train, y_train, X_test, y_test, model_name="lstm_model"):
    filepath = os.path.join(MODELS_DIR, f"{model_name}.h5")
    
    checkpoint = ModelCheckpoint(
        filepath, monitor='val_loss', verbose=1, 
        save_best_only=True, mode='min'
    )
    
    early_stopping = EarlyStopping(
        monitor='val_loss', patience=PATIENCE, verbose=1
    )
    
    history = model.fit(
        X_train, y_train,
        validation_data=(X_test, y_test),
        batch_size=BATCH_SIZE,
        epochs=EPOCHS,
        callbacks=[checkpoint, early_stopping],
        verbose=1
    )
    
    return history, model

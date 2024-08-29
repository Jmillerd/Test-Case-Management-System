# model_trainer.py

from transformers import Trainer, TrainingArguments
from test_case_generator import TestCaseGenerator
from datasets import Dataset

class ModelTrainer:
    def __init__(self, model_name='gpt2'):
        self.generator = TestCaseGenerator(model_name)
        self.model = self.generator.model
        self.tokenizer = self.generator.tokenizer

    def train(self, train_dataset):
        training_args = TrainingArguments(
            output_dir='./results',
            evaluation_strategy="epoch",
            learning_rate=2e-5,
            per_device_train_batch_size=4,
            num_train_epochs=3,
            weight_decay=0.01,
        )

        trainer = Trainer(
            model=self.model,
            args=training_args,
            train_dataset=train_dataset,
        )

        trainer.train()

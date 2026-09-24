package com.example.simplecalculator;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {

    private EditText editText;
    private String operator = "";
    private double operand1 = Double.NaN;
    private double operand2;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        editText = findViewById(R.id.editText);

        setupButtons();
    }

    private void setupButtons() {
        int[] numberButtonIds = {
                R.id.button0, R.id.button1, R.id.button2, R.id.button3,
                R.id.button4, R.id.button5, R.id.button6, R.id.button7,
                R.id.button8, R.id.button9
        };

        for (int id : numberButtonIds) {
            Button button = findViewById(id);
            button.setOnClickListener(this::onNumberClick);
        }

        Button buttonDot = findViewById(R.id.buttonDot);
        buttonDot.setOnClickListener(this::onDotClick);

        Button buttonAdd = findViewById(R.id.buttonAdd);
        Button buttonSub = findViewById(R.id.buttonSub);
        Button buttonMul = findViewById(R.id.buttonMul);
        Button buttonDiv = findViewById(R.id.buttonDiv);
        Button buttonEqual = findViewById(R.id.buttonEqual);

        buttonAdd.setOnClickListener(this::onOperatorClick);
        buttonSub.setOnClickListener(this::onOperatorClick);
        buttonMul.setOnClickListener(this::onOperatorClick);
        buttonDiv.setOnClickListener(this::onOperatorClick);
        buttonEqual.setOnClickListener(this::onEqualClick);
    }

    private void onNumberClick(View view) {
        Button button = (Button) view;
        editText.append(button.getText().toString());
    }

    private void onDotClick(View view) {
        if (!editText.getText().toString().contains(".")) {
            editText.append(".");
        }
    }

    private void onOperatorClick(View view) {
        Button button = (Button) view;
        operator = button.getText().toString();
        operand1 = Double.parseDouble(editText.getText().toString());
        editText.setText("");
    }

    private void onEqualClick(View view) {
        if (!operator.isEmpty()) {
            operand2 = Double.parseDouble(editText.getText().toString());
            double result = 0;

            switch (operator) {
                case "+":
                    result = operand1 + operand2;
                    break;
                case "-":
                    result = operand1 - operand2;
                    break;
                case "*":
                    result = operand1 * operand2;
                    break;
                case "/":
                    result = operand1 / operand2;
                    break;
            }

            editText.setText(String.valueOf(result));
            operator = "";
            operand1 = Double.NaN;
        }
    }
}

1.login detILS
2.when u click submit butn it go to 2nd activity there u have to displY Wlcme to my activity..

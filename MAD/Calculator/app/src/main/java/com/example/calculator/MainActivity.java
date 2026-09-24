package com.example.calculator;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

public class MainActivity extends AppCompatActivity {

    EditText t1;

    String firstNumber = "";
    String operator = "";

    boolean resultShown = false;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        t1 = findViewById(R.id.t1);

        // Number buttons
        int[] numberButtons = {
                R.id.b0, R.id.b1, R.id.b2, R.id.b3, R.id.b4,
                R.id.b5, R.id.b6, R.id.b7, R.id.b8, R.id.b9
        };

        for (int id : numberButtons) {
            Button button = findViewById(id);

            button.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View view) {

                    if (resultShown) {
                        t1.setText("");
                        resultShown = false;
                    }

                    t1.append(((Button) view).getText());
                }
            });
        }

        // Decimal button
        findViewById(R.id.b10).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {

                if (resultShown) {
                    t1.setText("");
                    resultShown = false;
                }

                String text = t1.getText().toString();

                if (!text.contains(".")) {

                    if (text.isEmpty()) {
                        t1.setText("0.");
                    } else {
                        t1.append(".");
                    }
                }
            }
        });

        // Backspace button
        findViewById(R.id.b11).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {

                String text = t1.getText().toString();

                if (!text.isEmpty()) {
                    t1.setText(text.substring(0, text.length() - 1));
                }
            }
        });

        // Addition
        findViewById(R.id.b12).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                setOperator("+");
            }
        });

        // Subtraction
        findViewById(R.id.b13).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                setOperator("-");
            }
        });

        // Multiplication
        findViewById(R.id.b14).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                setOperator("x");
            }
        });

        // Division
        findViewById(R.id.b15).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                setOperator("/");
            }
        });

        // Equal button
        findViewById(R.id.b16).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                calculate();
            }
        });

        // AC button
        findViewById(R.id.bac).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {

                t1.setText("");

                firstNumber = "";
                operator = "";
                resultShown = false;
            }
        });
    }

    // Set the selected operator
    private void setOperator(String selectedOperator) {

        String text = t1.getText().toString();

        if (text.isEmpty()) {
            return;
        }

        firstNumber = text;
        operator = selectedOperator;

        t1.setText("");
        resultShown = false;
    }

    // Perform calculation
    private void calculate() {

        String secondNumber = t1.getText().toString();

        if (firstNumber.isEmpty() || operator.isEmpty() || secondNumber.isEmpty()) {
            return;
        }

        double num1 = Double.parseDouble(firstNumber);
        double num2 = Double.parseDouble(secondNumber);

        double result = 0;

        switch (operator) {

            case "+":
                result = num1 + num2;
                break;

            case "-":
                result = num1 - num2;
                break;

            case "x":
                result = num1 * num2;
                break;

            case "/":

                if (num2 == 0) {
                    t1.setText("Error");
                    firstNumber = "";
                    operator = "";
                    resultShown = true;
                    return;
                }

                result = num1 / num2;
                break;
        }

        // Avoid displaying 5.0 when the answer is 5
        if (result == (long) result) {
            t1.setText(String.valueOf((long) result));
        } else {
            t1.setText(String.valueOf(result));
        }

        firstNumber = "";
        operator = "";
        resultShown = true;
    }
}
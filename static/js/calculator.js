// calculator.js - JavaScript para la calculadora web

// Variables globales
let currentNumber = '';
let previousNumber = '';
let operator = '';
let waitingForOperand = false;
let numbersList = [];
let history = [];

// Elementos del DOM
const basicDisplay = document.getElementById('basic-display');
const operationDisplay = document.getElementById('operation-display');
const scientificResult = document.getElementById('scientific-result');
const listResult = document.getElementById('list-result');
const numbersList_element = document.getElementById('numbers-list');
const historyList = document.getElementById('history-list');

// Funciones para calculadora básica
function appendNumber(number) {
    if (waitingForOperand) {
        currentNumber = number;
        waitingForOperand = false;
    } else {
        currentNumber = currentNumber === '0' ? number : currentNumber + number;
    }
    updateDisplay();
}

function setOperation(nextOperator) {
    const inputValue = parseFloat(currentNumber);

    if (previousNumber === '') {
        previousNumber = inputValue;
    } else if (operator) {
        const currentValue = previousNumber || 0;
        const newValue = performCalculation(currentValue, inputValue, operator);

        currentNumber = String(newValue);
        previousNumber = newValue;
    }

    waitingForOperand = true;
    operator = nextOperator;
    updateOperationDisplay();
}

function calculate() {
    const prev = parseFloat(previousNumber);
    const current = parseFloat(currentNumber);

    if (previousNumber === '' || operator === '') return;

    const result = performCalculation(prev, current, operator);
    
    // Agregar al historial
    addToHistory(`${previousNumber} ${getOperatorSymbol(operator)} ${currentNumber} = ${result}`);
    
    currentNumber = String(result);
    previousNumber = '';
    operator = '';
    waitingForOperand = true;
    updateDisplay();
    updateOperationDisplay();
}

function performCalculation(prev, current, operator) {
    const data = {
        operation: 'basic',
        num1: prev,
        num2: current,
        operator: operator
    };

    // Llamada a la API
    fetch('/api/calculate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            showError(data.error);
            return 0;
        }
        return data.result;
    })
    .catch(error => {
        showError('Error de conexión');
        return 0;
    });

    // Cálculo local como fallback
    switch (operator) {
        case '+': return prev + current;
        case '-': return prev - current;
        case '*': return prev * current;
        case '/': return current !== 0 ? prev / current : 0;
        case '//': return current !== 0 ? Math.floor(prev / current) : 0;
        case '%': return current !== 0 ? prev % current : 0;
        case '**': return Math.pow(prev, current);
        default: return current;
    }
}

function clearDisplay() {
    currentNumber = '0';
    previousNumber = '';
    operator = '';
    waitingForOperand = false;
    updateDisplay();
    updateOperationDisplay();
}

function deleteLast() {
    if (currentNumber.length > 1) {
        currentNumber = currentNumber.slice(0, -1);
    } else {
        currentNumber = '0';
    }
    updateDisplay();
}

function updateDisplay() {
    basicDisplay.textContent = currentNumber;
}

function updateOperationDisplay() {
    if (operator && previousNumber !== '') {
        operationDisplay.textContent = `${previousNumber} ${getOperatorSymbol(operator)}`;
    } else {
        operationDisplay.textContent = '';
    }
}

function getOperatorSymbol(op) {
    const symbols = {
        '+': '+',
        '-': '-',
        '*': '×',
        '/': '÷',
        '//': '÷÷',
        '%': 'mod',
        '**': '^'
    };
    return symbols[op] || op;
}

// Funciones para calculadora científica
function scientificFunction(func) {
    const number = parseFloat(document.getElementById('sci-number').value);
    
    if (isNaN(number)) {
        showScientificError('Por favor ingrese un número válido');
        return;
    }

    const data = {
        operation: 'advanced',
        function: func,
        number: number
    };

    fetch('/api/calculate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            showScientificError(data.error);
        } else {
            showScientificResult(data.result, `${getFunctionName(func)}(${number})`);
            addToHistory(`${getFunctionName(func)}(${number}) = ${data.result}`);
        }
    })
    .catch(error => {
        showScientificError('Error de conexión');
    });
}

function rootN() {
    const number = parseFloat(document.getElementById('root-number').value);
    const n = parseFloat(document.getElementById('root-n-value').value);
    
    if (isNaN(number) || isNaN(n)) {
        showScientificError('Por favor ingrese números válidos');
        return;
    }

    const data = {
        operation: 'advanced',
        function: 'root_n',
        number: number,
        n: n
    };

    fetch('/api/calculate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            showScientificError(data.error);
        } else {
            showScientificResult(data.result, `${n}√${number}`);
            addToHistory(`${n}√${number} = ${data.result}`);
        }
    })
    .catch(error => {
        showScientificError('Error de conexión');
    });
}

function getFunctionName(func) {
    const names = {
        'sqrt': '√',
        'factorial': '!',
        'ln': 'ln',
        'log10': 'log₁₀',
        'sin': 'sin',
        'cos': 'cos',
        'tan': 'tan'
    };
    return names[func] || func;
}

function showScientificResult(result, operation) {
    scientificResult.textContent = `${operation} = ${result}`;
    scientificResult.className = 'result-display success';
}

function showScientificError(error) {
    scientificResult.textContent = error;
    scientificResult.className = 'result-display error';
}

// Funciones para calculadora de listas
function addNumber() {
    const input = document.getElementById('number-input');
    const number = parseFloat(input.value);
    
    if (isNaN(number)) {
        alert('Por favor ingrese un número válido');
        return;
    }
    
    numbersList.push(number);
    input.value = '';
    updateNumbersList();
}

function removeNumber(index) {
    numbersList.splice(index, 1);
    updateNumbersList();
}

function updateNumbersList() {
    if (numbersList.length === 0) {
        numbersList_element.innerHTML = '<p class="empty-list">No hay números agregados</p>';
        return;
    }
    
    const listHTML = numbersList.map((number, index) => `
        <div class="number-item">
            <span>${number}</span>
            <button class="remove-number" onclick="removeNumber(${index})">×</button>
        </div>
    `).join('');
    
    numbersList_element.innerHTML = listHTML;
}

function listOperation(operation) {
    if (numbersList.length === 0) {
        showListError('No hay números en la lista');
        return;
    }

    const data = {
        operation: 'list',
        numbers: numbersList,
        operator: operation
    };

    fetch('/api/calculate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            showListError(data.error);
        } else {
            const operationName = getListOperationName(operation);
            showListResult(data.result, `${operationName}([${numbersList.join(', ')}])`);
            addToHistory(`${operationName}([${numbersList.join(', ')}]) = ${data.result}`);
        }
    })
    .catch(error => {
        showListError('Error de conexión');
    });
}

function getListOperationName(operation) {
    const names = {
        'sum': 'Suma',
        'subtract': 'Resta',
        'multiply': 'Multiplicación'
    };
    return names[operation] || operation;
}

function showListResult(result, operation) {
    listResult.textContent = `${operation} = ${result}`;
    listResult.className = 'result-display success';
}

function showListError(error) {
    listResult.textContent = error;
    listResult.className = 'result-display error';
}

function clearList() {
    numbersList = [];
    updateNumbersList();
    listResult.textContent = '';
    listResult.className = 'result-display';
}

// Funciones de historial
function addToHistory(calculation) {
    const timestamp = new Date().toLocaleTimeString();
    history.unshift({ calculation, timestamp });
    
    // Limitar historial a 50 elementos
    if (history.length > 50) {
        history = history.slice(0, 50);
    }
    
    updateHistoryDisplay();
}

function updateHistoryDisplay() {
    if (history.length === 0) {
        historyList.innerHTML = '<p class="empty-history">No hay cálculos en el historial</p>';
        return;
    }
    
    const historyHTML = history.map(item => `
        <div class="history-item">
            <span>${item.calculation}</span>
            <span class="history-time">${item.timestamp}</span>
        </div>
    `).join('');
    
    historyList.innerHTML = historyHTML;
}

function clearHistory() {
    history = [];
    updateHistoryDisplay();
}

// Funciones de utilidad
function showError(message) {
    basicDisplay.textContent = 'Error';
    operationDisplay.textContent = message;
    setTimeout(() => {
        clearDisplay();
    }, 2000);
}

// Soporte para teclado
document.addEventListener('keydown', function(event) {
    const key = event.key;
    
    // Números
    if (key >= '0' && key <= '9') {
        appendNumber(key);
    }
    
    // Operadores
    switch (key) {
        case '+':
            setOperation('+');
            break;
        case '-':
            setOperation('-');
            break;
        case '*':
            setOperation('*');
            break;
        case '/':
            event.preventDefault();
            setOperation('/');
            break;
        case 'Enter':
        case '=':
            event.preventDefault();
            calculate();
            break;
        case 'Escape':
            clearDisplay();
            break;
        case 'Backspace':
            event.preventDefault();
            deleteLast();
            break;
        case '.':
            appendNumber('.');
            break;
    }
});

// Inicialización
document.addEventListener('DOMContentLoaded', function() {
    updateDisplay();
    updateNumbersList();
    updateHistoryDisplay();
});

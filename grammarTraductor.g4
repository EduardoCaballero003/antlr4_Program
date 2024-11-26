grammar grammarTraductor;

// Tokens del lexer
DEF: 'def';
RETURN: 'return';
PRINT: 'print';
ID: [a-zA-Z_][a-zA-Z_0-9]*;
LPAREN: '(';
RPAREN: ')';
COMMA: ',';
TWOPOINTS: ':';
NUMERO: [0-9]+;
TAB: '\t';
JUMP: '\n';

//Operaciones
MUL: '*';
DIV: '/';
ADD: '+';
SUB: '-';
EQUAL : '=';

// La regla principal del parser
program: statement+;

statement: functionDef | printResults;

functionDef: DEF ID LPAREN paramList? RPAREN TWOPOINTS statements;

statements: return | igualation | printStatement;

paramList: param (COMMA param)*;
param: ID;

paraNumberList: paramNumber (COMMA paramNumber);
paramNumber: NUMERO;

return: RETURN expression;

igualation: ID EQUAL expression;

expression: NUMERO 
          | ID 
          | expression MUL expression 
          | expression ADD expression
          | expression SUB expression
          | expression DIV expression
          | LPAREN expression RPAREN;

printStatement: PRINT LPAREN expression RPAREN; 

printResults: PRINT LPAREN ID LPAREN paraNumberList? RPAREN RPAREN;

// Espacios en blanco y comentarios (ignorados)
WS: [ \t\r\n]+ -> skip;

// Error de token
ERROR: .;

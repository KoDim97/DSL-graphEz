grammar graphEzGrammar;

program: graph+ ;
graph:
        '{' 
           render?
           elements
        '}';

render: '['
            layout?
            extension?
        ']';
        
layout: 'layout' ('dot' | 'neato' | 'twopi' | 'circo' | 'graphs' | 'fdp' | 'sfdp') ;

extension: 'extension' ('png' | 'dot' | 'jpg' | 'jpeg' | 'pdf' | 'ps' | 'svg') ;

elements: element+ ;

element:   (    (vertex) |
                (vertex edge vertex weight?)
           ) ;

vertex: TEXT ;
TEXT: [a-zA-Z][.a-zA-Z_0-9]* ;

weight: INTEGER ;

INTEGER: [0-9]+ ;

edge: ('->' | '<-' | '-') ;

SPACE: [ \t\r\n] -> skip;
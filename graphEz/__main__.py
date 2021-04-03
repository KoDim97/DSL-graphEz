# That file was generated automatically with DSL editor
# The moment of generation: 02/04/2021 23:09:42


import sys
from antlr4 import *
from antlr4.Utils import escapeWhitespace
from antlr4.tree.Trees import Trees
from graphEz.graphEzGrammarLexer import graphEzGrammarLexer
from graphEz.graphEzGrammarParser import graphEzGrammarParser
from antlr4.error.ErrorListener import *
from graphEz.Pipeline import Pipeline

class ChatErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise Exception('line ' + str(line) + ':' + str(column) + ':' + msg)


level = 0

def toPrettyTree(t, ruleNames):
    global level
    level = 0
    return process(t, ruleNames).replace("(?m)^\\s+$", "").replace("\\r?\\n\\r?\\n", "\n")

def process(t, ruleNames):
    global level
    if t.getChildCount() == 0:
        return escapeWhitespace(Trees.getNodeText(t, ruleNames), False)
    sb = ""
    sb += lead(level)
    level += 1
    s = escapeWhitespace(Trees.getNodeText(t, ruleNames), False)
    sb += (s + ' ')
    for i in range(t.getChildCount()):
    	sb += process(t.getChild(i), ruleNames)
    level -= 1
    # sb += lead(level)
    return sb

def lead(level):
    sb = ""
    if (level > 0):
    	sb += "\n"
    	for cnt in range(level):
    		sb += " "
    return sb

def node2diagram(t, left, names, f, counter, gen):
    n = t.getChildCount()
    print(counter, '[label = "', left.replace('"','\\"'), '"]', sep='', file=f)
    for i in range(0, n):
        right = t.getChild(i)
        nxt = next(gen)
        if right.getChildCount() == 0:
            print(nxt, '[label = "', right.getText().replace('"','\\"'), '"]', sep='', file=f)
            print(counter, '->', nxt, sep='', file=f)
        else:
            print(nxt, '[label = "', names[right.getRuleIndex()], '"]', sep='', file=f)
            print(counter, '->', nxt, sep='', file=f)
            node2diagram(t.getChild(i), names[right.getRuleIndex()].replace('"','\\"'), names, f, nxt, gen)


def tree2diagram(t, names):
    f = open("graphEzGrammar.dot", "w")
    print("digraph {", sep='', file=f)

    gen = (x for x in range(100000))

    node2diagram(t, names[t.getRuleIndex()], names, f, next(gen), gen)

    print("}", sep='', file=f)
    f.close()


class GraphContainer:
    def __init__(self):
        self.layout = 'dot'
        self.extension = 'png'
        self.elements = []


class ElementContainer:
    def __init__(self):
        self.src = None
        self.dst = None
        self.edge = None
        self.weight = None


def parse_render_options(render, graph_class):
    n = render.getChildCount()
    for i in range(n):
        child = render.getChild(i)
        if isinstance(child, graphEzGrammarParser.LayoutContext):
            graph_class.layout = child.children[1].symbol.text
        elif isinstance(child, graphEzGrammarParser.ExtensionContext):
            graph_class.extension = child.children[1].symbol.text


def parse_element(element):
    element_class = ElementContainer()
    n = element.getChildCount()
    for i in range(n):
        child = element.getChild(i)
        if isinstance(child, graphEzGrammarParser.VertexContext):
            if element_class.src is None:
                element_class.src = child.children[0].symbol.text
            elif element_class.dst is None:
                element_class.dst = child.children[0].symbol.text
        elif isinstance(child, graphEzGrammarParser.EdgeContext):
            if child.children[0].symbol.text == '-':
                element_class.edge = 'none'
            elif child.children[0].symbol.text == '->':
                element_class.edge = 'forward'
            elif child.children[0].symbol.text == '<-':
                element_class.edge = 'back'
        elif isinstance(child, graphEzGrammarParser.WeightContext):
                element_class.weight = int(child.children[0].symbol.text)
    return element_class


def parse_elements(elements, graph_class):
    n = elements.getChildCount()
    elements_list = []
    for i in range(n):
        child = elements.getChild(i)
        if isinstance(child, graphEzGrammarParser.ElementContext):
            elements_list.append(parse_element(child))
    graph_class.elements = elements_list


def parse_graph(graph):
    graph_class = GraphContainer()
    n = graph.getChildCount()
    for i in range(n):
        child = graph.getChild(i)
        if isinstance(child, graphEzGrammarParser.RenderContext):
            parse_render_options(child, graph_class)
        elif isinstance(child, graphEzGrammarParser.ElementsContext):
            parse_elements(child, graph_class)
    return graph_class

def main(argv):
    input = FileStream(argv[1], encoding='utf-8')
    lexer = graphEzGrammarLexer(input)
    stream = CommonTokenStream(lexer)
    parser = graphEzGrammarParser(stream)
    error_listener = ChatErrorListener()
    parser.addErrorListener(error_listener)

    graphs = []
    try:
        program = parser.program()
    except Exception as e:
        return
    n = program.getChildCount()
    for i in range(n):
        child = program.getChild(i)
        if isinstance(child, graphEzGrammarParser.GraphContext):
            graphs.append(parse_graph(child))
    ciao_pipeline = Pipeline(graphs)
    ciao_pipeline.entryPipeline()

    # ast = syntaxVisitor().visitRulelist(tree)
    # print(tree.toStringTree(recog=parser))
    # print(parser.ruleNames)
    # print(toPrettyTree(tree, parser.ruleNames))
    # print(tree.toStringTree(recog=parser))
    # tree2diagram(tree, parser.ruleNames)
    # print(parser.ruleNames[tree.getChild(0).getRuleIndex()], " ", parser.ruleNames)


if __name__ == '__main__':
    main(sys.argv)

# That file was generated automatically with DSL editor
# The moment of generation: 03/04/2021 00:53:15
import pygraphviz as pgv
import time
import os


class Pipeline:

    #VARS
    def __init__(self, graphList):
        self.curGraph = None
        self.graphList = graphList
        self.size = len(graphList)
        self.__state__ = "entry"

    #INNER
    def __hasWork(self):
        return len(self.graphList) != 0

    def __nextGraph(self):
        return Graph(self.graphList.pop())

    def __printInfo(self):
        cwd = os.getcwd()
        print(self.size, f'graphs successfully saved in {cwd}\output')

    #PROVIDED
    def entryPipeline(self):
        self.run()

    def run(self):
        while (True):
            if self.__state__ == "exit":
                break
            if self.__state__ == "entry" :
                if True:
                    self.curGraph = self.__nextGraph()
                    self.__state__ = "ready_treat"
                    continue
            if self.__state__ == "ready_treat" :
                if True:
                    self.curGraph.entryGraph()
                    self.__state__ = "finish_treat"
                    continue
            if self.__state__ == "finish_treat" :
                if self.__hasWork():
                    self.curGraph = self.__nextGraph()
                    self.__state__ = "ready_treat"
                    continue
                self.__printInfo()
                self.__state__ = "exit"
                continue


class Graph:

    #VARS
    def __init__(self, graphDesc):
        self.graph = pgv.AGraph()
        self.layout = graphDesc.layout
        self.extension = graphDesc.extension
        self.curElement = None
        self.elementList = graphDesc.elements
        self.__state__ = "entry"

    #INNER
    def __hasElement(self):
       return len(self.elementList) != 0

    def __nextElement(self):
        return Element(self.graph, self.elementList.pop())

    def __renderGraph(self):
        local_time = time.localtime()
        opt = time.strftime("graphEz_%d%m%Y_%H%M%S", local_time)
        if not os.path.exists('output'):
            os.makedirs('output')
        self.graph.draw(f'output\{opt}.{self.extension}', prog=self.layout)

    #PROVIDED
    def entryGraph(self):
        self.run()

    def run(self):
        while (True):
            if self.__state__ == "exit":
                break
            if self.__state__ == "entry" :
                if True:
                    self.curElement = self.__nextElement()
                    self.__state__ = "ready_treat"
                    continue
            if self.__state__ == "ready_treat" :
                if True:
                    self.curElement.entryElement()
                    self.__state__ = "finish_treat"
                    continue
            if self.__state__ == "finish_treat" :
                if self.__hasElement():
                    self.curElement = self.__nextElement()
                    self.__state__ = "ready_treat"
                    continue
                self.__renderGraph()
                self.__state__ = "exit"
                continue


class Element:

    #VARS
    def __init__(self, graph, elementDesc):
        self.graph = graph
        self.src = elementDesc.src
        self.dst = elementDesc.dst
        self.edge = elementDesc.edge
        self.weight = elementDesc.weight
        self.__state__ = "entry"

    #INNER
    def __addElement(self):
        if self.dst is None:
            self.graph.add_node(self.src)
            return
        if self.weight is None:
            self.graph.add_edge(self.src, self.dst, dir=self.edge)
        else:
            self.graph.add_edge(self.src, self.dst, dir=self.edge, label=self.weight)
    #PROVIDED
    def entryElement(self):
        self.run()

    def run(self):
        while (True):
            if self.__state__ == "exit":
                break
            if self.__state__ == "entry" :
                if True:
                    self.__addElement()
                    self.__state__ = "exit"
                    continue



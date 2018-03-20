# -*- coding: utf-8 -*-
from .problem import Problem
from .action import  Action
from .task_index import TaskIndex
from .fstrips import Effect, AddEffect, DelEffect, FunctionalEffect, UniversalEffect, language

def create_fs_task(problem):
    """ Create a problem domain and instance and perform the appropriate validity checks """
    domain_name = problem.language.name
    instance_name = problem.name

    task = TaskIndex(domain_name, instance_name)
    task.process_symbols(problem)
    task.process_state_variables()
    #task.process_initial_state(problem.init)
    #task.process_actions(problem.actions)
    #task.process_processes([])
    #task.process_events([])
    #task.process_goal(problem.goal)
    # @TODO: differentiate state constraints and axioms
    #task.process_state_constraints(problem.constraints)
    #task.process_axioms(fd_task.axioms)
    # @TODO: no metric for these guys?
    #task.process_metric(None)
    return task


def create_fs_plus_task(problem):
    """ Create a problem domain and instance and perform the appropiate validty checks """
    task = TaskIndex(domain_name, instance_name)
    task.process_symbols(problem)
    task.process_state_variables()
    #task.process_initial_state(problem.init)
    #task.process_actions(problem.actions)
    #task.process_processes(problem.processes)
    #task.process_events(problem.events)
    #task.process_goal(problem.goal)
    #task.process_state_constraints(problem.constraints)
    #task.process_lifted_state_constraints(problem.constraint_schemata)
    #task.process_axioms(problem.axioms)
    #task.process_metric(problem.metric)
    return task

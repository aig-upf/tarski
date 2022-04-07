# tarski: An AI Planning Modeling Framework
#
# Author: Miquel Ramirez <miquel.ramirez@pm.me>
# ----------------------------------------------------------------------------------------------------------------------
# src/tarski/io/sas/fd.py
#
# SAS instance writer for Fast Downward pre-processor
# ----------------------------------------------------------------------------------------------------------------------
from tarski.io.sas.templates import variable_section_elem_tmpl, axiom_defaults_section_tmpl, precondition_elem_tmpl, \
    effect_elem_tmpl, operator_tmpl, initial_value_list_elem_tmpl, initial_state_section_tmpl, \
    goal_value_list_elem_tmpl, goal_state_section_tmpl, sas_instance_tmpl
from tarski.syntax import symref, CompoundTerm


FAST_DOWNWARD_SAS_VERSION = 4


class Writer(object):

    def __init__(self, **kwargs):
        self.dom_theory = kwargs['theory']
        self.state_variables = kwargs['state_variables']
        self.domains = kwargs['domains']
        self.actions = kwargs['actions']
        self.initial = kwargs['initial']
        self.goal = kwargs['goal']
        self.unit_costs = kwargs.get('unit_costs', True)

    def get_sas_version(self) -> str:
        return '{}'.format(FAST_DOWNWARD_SAS_VERSION)

    def get_metric_type(self) -> str:
        return '{}'.format(self.unit_costs and 0 or 1)

    def get_number_variables(self) -> str:
        return '{}'.format(len(self.state_variables))

    def make_value_section(self, var: CompoundTerm) -> str:
        """
        Makes values section in variable definition section
        :param var:
        :return:
        """
        value_list = []
        for obj in self.domains[symref(var)].objects:
            value_list += ['{}'.format(str(obj.expr))]
        return '\n'.join(value_list)

    def make_variable_section(self) -> str:
        elements = []
        for var in self.state_variables:
            elements += [variable_section_elem_tmpl.substitute(
                name=str(var.expr),
                # @TODO: come up with proper value when we get axioms in fully
                axiom_layer=-1,
                domain_size=len(self.domains[var]),
                value_section=self.make_value_section(var.expr)
            )]

        return '\n'.join(elements)

    def get_number_mutex_groups(self) -> str:
        """
        Returns the number of mutex groups in the instance
        :return:
        """
        # @TODO: review this when we come up with an idea of what are these constraints exactly
        return '{}'.format(0)

    def make_mutex_group_section(self) -> str:
        """
        Constructs the mutex group section of the SAS instance file
        :return:
        """
        mutex_groups = []

        # @TODO: implement when we have an idea of what are these constraints exactly
        if len(mutex_groups) == 0:
            return ''

        return "\n".join(mutex_groups)

    def make_axioms_defaults_list(self) -> str:
        defaults = []

        # @TODO: finish implementation when we have axioms in
        if len(defaults) == 0:
            return ''
        return '\n' + '\n'.join(defaults)

    def make_axiom_defaults_section(self) -> str:
        # @TODO: finish implementation when we have axioms in
        return axiom_defaults_section_tmpl.substitute(
            num_axiom_vars=0,
            axiom_defaults_list=self.make_axioms_defaults_list()
        )

    def get_number_axiom_rules(self) -> str:
        # @TODO: finish implementation when we have axioms fully in
        return '{}'.format(0)

    def make_axiom_rules_section(self) -> str:
        rules = []

        # @TODO: finish implementation when we have it
        if len(rules) == 0:
            return ''
        return '\n' + '\n'.join(rules)

    def get_num_operators(self):
        return '{}'.format(len(self.actions))

    def get_action_name(self, a):
        return "{}({})".format(a.name, ",".join([str(arg) for arg in a.arguments]))

    def get_num_preconditions(self, a):
        return len(a.transitions)

    def make_precondition_list(self, a):
        elems = []
        for x, v, _ in a.transitions:
            elems += [precondition_elem_tmpl.substitute(
                variable_index=self.state_variables.get_index(symref(x)),
                value_index=self.domains[symref(x)].get_index(symref(v))
            )]
        return '\n'.join(elems)

    def get_num_effects(self, a):
        return len(a.transitions)

    def make_effect_list(self, a):
        elems = []

        for x, _, w in a.transitions:
            elems += [effect_elem_tmpl.substitute(
                num_effect_conditions=0,
                effect_condition_list='',
                affected_variable_index=self.state_variables.get_index(symref(x)),
                new_value_index=self.domains[symref(x)].get_index(symref(w))
            )]

        return '\n'.join(elems)

    def get_cost(self, a):
        # @TODO: finish implementation when we have action costs
        return '{}'.format(1)

    def make_operators_section(self):
        """
        Constructs the operators section
        :return:
        """
        operators = []
        assert len(self.actions) > 0
        for action in self.actions:
            operators += [operator_tmpl.substitute(
                name=self.get_action_name(action),
                num_preconditions=self.get_num_preconditions(action),
                precondition_list=self.make_precondition_list(action),
                num_effects=self.get_num_effects(action),
                effect_list=self.make_effect_list(action),
                cost=self.get_cost(action)
            )]
        print(operators)
        return '\n'.join(operators)

    def make_initial_value_list(self) -> str:
        """

        :return:
        """
        values = []
        for x, v in self.initial:
            values += [initial_value_list_elem_tmpl.substitute(
                variable_index=self.state_variables.get_index(symref(x)),
                value_index=self.domains[symref(x)].get_index(symref(v))
            )]

        return '\n'.join(values)

    def make_initial_state_section(self) -> str:
        return initial_state_section_tmpl.substitute(
            num_variables=len(self.state_variables),
            initial_value_list=self.make_initial_value_list()
        )

    def make_goal_value_list(self) -> str:
        values = []
        for x, v in self.goal:
            values += [goal_value_list_elem_tmpl.substitute(
                variable_index=self.state_variables.get_index(symref(x)),
                value_index=self.domains[symref(x)].get_index(symref(v))
            )]
        return '\n'.join(values)

    def make_goal_state_section(self) -> str:
        return goal_state_section_tmpl.substitute(
            goal_value_list=self.make_goal_value_list()
        )

    def dump(self, fp) -> None:
        """
        Dumps instance data in file-like object `fp`
        :param fp:
        :return:
        """

        data = sas_instance_tmpl.substitute(
            format_version=self.get_sas_version(),
            metric_type=self.get_metric_type(),
            num_variables=self.get_number_variables(),
            variable_section=self.make_variable_section(),
            num_mutex_groups=self.get_number_mutex_groups(),
            mutex_group_section=self.make_mutex_group_section(),
            axiom_defaults_section=self.make_axiom_defaults_section(),
            num_axiom_rules=self.get_number_axiom_rules(),
            axiom_rules_section=self.make_axiom_rules_section(),
            num_operators=self.get_num_operators(),
            operators_section=self.make_operators_section(),
            initial_state_section=self.make_initial_state_section(),
            goal_state_section=self.make_goal_state_section()
        )

        fp.write(data)

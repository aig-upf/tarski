# tarski: An AI Planning Modeling Framework
#
# Author: Miquel Ramirez <miquel.ramirez@pm.me>
# ----------------------------------------------------------------------------------------------------------------------
# src/tarski/io/sas/templates.py
#
# Templates for Fast Downward SAS instance structure
#
# Source: https://www.fast-downward.org/TranslatorOutputFormat4
# ----------------------------------------------------------------------------------------------------------------------

from string import Template

value_section_elem_tmpl = Template("""\
Atom ${value_symbol}""")

value_section_null_tmpl = Template("""\
<none of those>""")

variable_section_elem_tmpl = Template("""\
begin_variable
${name}
${axiom_layer}
${domain_size}
${value_section}
end_variable""")

mutex_group_list_element_tmpl = Template("""\
${index_v} ${index_value}""")

mutex_group_section_elem_tmpl = Template("""\
begin_mutex_group
${group_size}
${mutex_group_list}
end_mutex_group""")

axiom_defaults_list_elem_tmpl = Template("""\
${variable_index} ${default_value_index}""")

axiom_defaults_section_tmpl = Template("""\
begin_axiom_defaults
${num_axiom_vars}${axiom_defaults_list}
end_axiom_defaults""")

axiom_rule_condition_tmpl = Template("""\
${variable_index} ${value_index}""")

axiom_rule_tmpl = Template("""\
begin_rule
${axiom_rule_condition}
${axiom_head_index} ${axiom_head_value}
end_rule""")

precondition_elem_tmpl = Template("""\
${variable_index} ${value_index}""")

effect_elem_tmpl = Template("""\
${num_effect_conditions} ${effect_condition_list} ${affected_variable_index} ${new_value_index}""")

operator_tmpl = Template("""\
begin_operator
${name}
${num_preconditions}
${precondition_list}
${num_effects}
${effect_list}
${cost}
end_operator""")

initial_value_list_elem_tmpl = Template("""\
${variable_index} ${value_index}""")

initial_state_section_tmpl = Template("""\
begin_initial_state
${num_variables}
${initial_value_list}
end_initial_state""")

goal_value_list_elem_tmpl = Template("""\
${variable_index} ${value_index}""")

goal_state_section_tmpl = Template("""\
begin_goal
${goal_value_list}
end_goal""")

sas_instance_tmpl = Template("""\
begin_version
${format_version}
end_version
begin_metric
${metric_type}
end_metric
${num_variables}
${variable_section}
${num_mutex_groups}${mutex_group_section}
${axiom_defaults_section}
${num_axiom_rules}${axiom_rules_section}
${num_operators}
${operators_section}
${initial_state_section}
${goal_state_section}
""")

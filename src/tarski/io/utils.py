import os


def find_domain_filename(task_filename):
    """ Find domain filename for the given task using the standard automatic naming rules used in the IPCs.
    Return None if no domain filename could be found according to those rules.
    The code here is taken quasi-verbatim from Fast Downward's preprocessor
    <http://hg.fast-downward.org/file/ea4f6e86af18/driver/util.py#l27>
    """
    dirname, basename = os.path.split(task_filename)

    domain_basenames = [
        "domain.pddl",
        basename[:3] + "-domain.pddl",
        "domain_" + basename,
        "domain-" + basename,
    ]

    for domain_basename in domain_basenames:
        domain_filename = os.path.join(dirname, domain_basename)
        if os.path.exists(domain_filename):
            return domain_filename

    return None

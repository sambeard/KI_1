# analysis.py
# -----------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


######################
# ANALYSIS QUESTIONS #
######################

# Set the given parameters to obtain the specified policies through
# value iteration.

def question2():
    answerDiscount = 0.9
    answerNoise = 0.01694       #changed
    return answerDiscount, answerNoise

def question3a():
    # close exit, risk cliff
    answerDiscount = 0.9        # regular discount
    answerNoise = 0.1           # slightly lower noise
    answerLivingReward = -5.0   # high negativeliving reward
    return answerDiscount, answerNoise, answerLivingReward

def question3b():
    # close exit, avoid cliff
    answerDiscount = 0.3        # high discount factor
    answerNoise = 0.2           # regular noise
    answerLivingReward = -0.5   # regular negative living reward
    return answerDiscount, answerNoise, answerLivingReward

def question3c():
    # distant exit, risk cliff
    answerDiscount = 0.9        # regular discount factor
    answerNoise = 0.0           # no noise
    answerLivingReward = -2     # relatively high negative living reward
    return answerDiscount, answerNoise, answerLivingReward

def question3d():
    # distant exit, avoid cliff
    answerDiscount = 0.9        # regular discount reward
    answerNoise = 0.2           # regular noise
    answerLivingReward = 0      # no living reward
    return answerDiscount, answerNoise, answerLivingReward

def question3e():
    # avoid all terminal states
    answerDiscount = 0.9        # regular discount reward
    answerNoise = 0.2           # regular noise
    answerLivingReward = 1      # positive living reward
    return answerDiscount, answerNoise, answerLivingReward

def question6():
    answerEpsilon = None
    answerLearningRate = None
    return answerEpsilon, answerLearningRate
    # If not possible, return 'NOT POSSIBLE'

if __name__ == '__main__':
    print 'Answers to analysis questions:'
    import analysis
    for q in [q for q in dir(analysis) if q.startswith('question')]:
        response = getattr(analysis, q)()
        print '  Question %s:\t%s' % (q, str(response))

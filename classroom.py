import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw_classroom():
    fig, ax = plt.subplots(figsize=(10, 6))

    classroom = patches.Rectangle((0, 0), 10, 6, edgecolor='black', facecolor='lightblue')
    ax.add_patch(classroom)

    desk_positions = [(1, 2.5), (4, 2.5), (7, 2.5),
                      (1, 0.5), (4, 0.5), (7, 0.5)] 

    for pos in desk_positions:
        desk = patches.Rectangle(pos, 2, 1, edgecolor='black', facecolor='tan')
        ax.add_patch(desk)

    blackboard = patches.Rectangle((0.5, 5), 9, 0.5, edgecolor='black', facecolor='black')
    ax.add_patch(blackboard)

    teacher_desk = patches.Rectangle((4, 4), 2, 1, edgecolor='black', facecolor='brown')
    ax.add_patch(teacher_desk)

    ax.text(4.3, 5.1, 'Blackboard', fontsize=10, color='white')
    ax.text(4.3, 4.5, 'Teacher\'s Desk', fontsize=10, color='white')

    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.set_title('Classroom Layout')
    ax.set_xticks([])
    ax.set_yticks([])

    plt.show()

draw_classroom()

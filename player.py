class Player:
    """Represents the player character, much more to come"""

    def __init__(self, name):
        self.name = name
        self.health = 100
        self.current_weapon = None
        self.current_armor = None
        self.inventory = {
            "weapons": [],
            "health": [],
            "armor": [],
            "spells": []
        }
        self.damage_base = 5
        self.equipped = ""
        self.current_cap_tool = ""
        self.puppets = []

    def damage_modifier(self):
        return self.current_weapon.damage + self.damage_base

    def armor_modifier(self):
        return self.current_armor.health_mod + self.health

    def pick_up_item(self, item):
        if item.type == "weapon":  # This will get changed back once we
            self.inventory['weapons'].append(item)
        elif item.type == "health":
            self.inventory['health'].append(item)
        elif item.type == "armor":
            self.inventory['armor'].append(item)
        elif item.type == "spell":
            self.inventory['spells'].append(item)
        else:
            print("Wtf are you doing Ryan")

    def equip_item(self, item):
        if item.type == "weapon":
            if item in self.inventory['weapons']:
                self.inventory['weapons'].append(self.current_weapon)
                self.inventory['weapons'].remove(item)
                self.current_weapon = item
        elif item.type == "armor":
            if item in self.inventory['armor']:
                self.inventory['armor'].append(self.current_armor)
                self.inventory['armor'].remove(item)
                self.current_armor = item
        else:
            print("Wtf are you doing Ryan")

    def equipped_items(self):
        if len(self.puppets) == 0:
            self.equipped = f"""
Your current Equipped items: 
    Weapon: {self.current_weapon.name}
    Armor: {self.current_armor.name}
    Capture Device: {self.current_cap_tool.name}
    
You current stats: 
    Health: {self.health}
    Armor modifier: {self.armor_modifier()}
    Damage dealt: {self.damage_modifier()}
"""
        else:
            self.equipped = f"""
Your current Equipped items: 
    Weapon: {self.current_weapon.name}
    Armor: {self.current_armor.name}
    Capture Device: {self.current_cap_tool.name}
    
You current stats: 
    Health: {self.health}
    Armor modifier: {self.armor_modifier()}
    Damage dealt: {self.damage_modifier()}
    Puppets: {', '.join(puppet.name for puppet in self.puppets)}"""
        return self.equipped

    def capture_puppet(self, puppet):
        self.puppets.append(puppet)
        return input(f"You have added {puppet.name} to the puppet show. "
                     f"Enjoy " \
                     f"your new puppet, Puppet Master!")

    def show_inventory(self):
        spells = '\r\n\t'.join(
            spell.name for spell in self.inventory['spells'])
        healthpotions = '\r\n\t'.join(potion.name for potion in self.inventory[
            'health'])
        weapons = '\r\n\t'.join(weapon.name for weapon in self.inventory[
            'weapons'])
        armor = '\r\n\t'.join(armor.name for armor in self.inventory['armor'])
        print(f"""
Spells:
    {spells}
Armor: 
    {armor}
Weapons: 
    {weapons}
Health: 
    {healthpotions}
""")

    def take_health_potion(self):
        potion = self.inventory['health'][0]
        self.health = potion.amount
        self.inventory['health'].pop()
        print(f"You have taken {potion.name} and restored you health to "
              f"{self.health}")

    def puppet_play(self):
        puppets = self.puppets
        input("Which puppet would you like to play with?")

        print(f"""
You guide the puppet to a secluded room, the sound of your 
synchronized footsteps echoing softly against the bare walls. The 
door shuts with a definitive click behind you. It's just you and the 
puppet now, enveloped in the dim, warm light that casts shadows 
across his anxious face.

"Sit," you command gently, pointing towards the edge of the bed. He 
complies, the mattress creaking under his weight as he watches you with a 
mix of nervousness and excitement. You can see his chest rise and fall more 
rapidly—anticipation building.

Approaching him, you maintain eye contact, an unspoken promise lingering in 
your gaze. Reaching his side, you swiftly kneel in front of him, 
your fingers deftly moving to his belt. The metal buckle clinks as it comes 
undone, a sharp yet inviting sound in the quiet room. You methodically 
unbutton his pants and slowly pull down the zipper, the sound slicing 
through the thick air.

His pants are now loose, and you slide them down his legs, revealing his 
fully erect cock, which stands proud and eager. You pause for a moment, 
allowing the tension to build, your hot breath brushing against his skin 
causing him to shiver in anticipation.

"You're mine to enjoy," you murmur, your voice a sultry whisper that sends a 
jolt through his body. Leaning in, you let your tongue peek out slightly, 
touching the base of his cock. Slowly, deliberately, you drag your tongue up 
the length of his shaft, savoring the salty taste of his skin and the 
throbbing pulse beneath. Reaching the tip, you encircle it with your lips, 
teasing gently before taking him fully into your mouth.

The room is filled with the soft, wet sounds of your lips and tongue working 
his cock, mixed with his stifled moans. You set a rhythm, bobbing your head 
slowly at first, then increasing in pace, driven by the urgent sounds of his 
pleasure.While continuing to pleasure him with your mouth, you unbutton your 
own pants with one hand, pushing them down just enough to expose your wet, 
eager pussy. You pull away from his cock momentarily, your lips making a 
soft 'pop' as they release him.

"Touch me," you command breathily, grabbing his hand and guiding it between 
your legs. His fingers are hesitant at first, lightly tracing the outer lips 
of your pussy. You moan softly, encouraging him, "More, don't be shy."

With a growing confidence spurred by your moans, he presses a finger against 
your slick entrance, exploring the wetness before slipping inside. The 
sensation sends a shiver through your body, and you moan louder, feeling the 
build-up of pleasure. 

You return to his cock, now even more aroused than before, taking him deep 
into your mouth again. The room fills with the symphony of your combined 
moans and the wet sounds of his finger moving inside you. His thumb finds 
your clit, rubbing in tight circles, heightening your pleasure to near 
unbearable levels.

As you suck and lick, his finger continues their dance inside you, driving 
you both towards climax. Your body begins to tremble, signaling the 
approaching wave of orgasm.Pulling away from his cock, you stand up, 
your breath heavy with arousal. "Bend me over," you command huskily, turning 
around and leaning forward against the bed. Your ass is presented invitingly 
to him, your pants still haphazardly hanging around your thighs.

He hesitates for just a moment, overwhelmed by the sight, before his desire 
takes over. Stepping up behind you, he positions himself at your entrance, 
his hands gripping your hips firmly. You feel the head of his cock nudging 
against you, teasing the slick, sensitive folds.

"Fuck me," you demand, pushing back against him, eager to feel him inside 
you. With a firm thrust, he sinks into you, filling you completely. A loud 
moan escapes your lips as he begins to move, his thrusts initially tentative 
but quickly gaining confidence and speed.

The room echoes with the sound of skin slapping against skin as he fucks you 
from behind, his grip on your hips tightening. You encourage him with every 
thrust, your voice a mix of moans and dirty talk, urging him to go harder 
and deeper.

Your hands clutch the sheets, pleasure building within you as he hits all 
the right spots. You glance back at him over your shoulder, meeting his eyes 
with a lustful gaze, driving him even further into a frenzy.

The intensity of his thrusts increases, and you feel your climax building, 
unstoppable and fierce.His breaths grow heavier, more desperate as he 
continues to thrust into you, approaching his own limit. "Please, may I...?" 
he stammers out between labored breaths, the plea barely escaping his lips 
as he struggles to hold back, waiting for your approval.

You let out a satisfied moan, feeling the waves of your own climax begin to 
subside. "Yes, you can cum now," you grant him permission, your voice both 
commanding and sultry. Relief washes over his face, mixed with intense 
pleasure, as he gives into the sensation.

His movements become more frenzied, erratic as he chases his climax, spurred 
on by your permission. You feel him swell inside you, his cock pulsating as 
he reaches his edge. With a deep, guttural moan, he releases, filling you 
with warmth as he collapses slightly against your back, both of you panting 
heavily from the intensity of the experience.

After a moment, he pulls out gently, both of you fixing your attire as you 
prepare to leave the secluded room""")

